from app.models import Users ,Sale,Lead
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from braces.views import CsrfExemptMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.db.utils import IntegrityError
from datetime import datetime,timedelta
from django.db.models import Q
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple
class SalesView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        try:
            lead_ids=request.data.get('lead_ids')
            lead_ids = [int(lead_id) for lead_id in lead_ids]
            assignee_id=request.data.get('assignee_id')
            assignee_instance=Users.objects.get(pk=assignee_id)
            leads=Lead.objects.filter(pk__in=lead_ids)
            
            user_instance=request.user
            if user_instance.role.name == "admin" or user_instance.role.name == "leads":
                with transaction.atomic():
                    sales_instance= [Sale(
                        lead=lead_id,
                        assignee=assignee_instance
                    )for lead_id in leads]

                    for lead in leads:
                        lead.is_assigned = True
                        lead.save()

                    Sale.objects.bulk_create(sales_instance)
                    
            else:
                return JsonResponse({"message":"Sorry! You can not add sale"},status=status.HTTP_401_UNAUTHORIZED)
                
        except IntegrityError as i:
            return JsonResponse({"message":str(i)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return JsonResponse({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
        return JsonResponse({'message':f"Leads assigned successfully to {assignee_instance.name}"},status=status.HTTP_201_CREATED)
        
    
    def get(self, request):
        try:
            pageNo = request.GET.get("page_no")
            client_name = request.GET.get('client_name') if request.GET.get('client_name') else None
            contact_no = request.GET.get('contact_no') if request.GET.get('contact_no') else None
            date_range=request.GET.get('date_range') if request.GET.get('date_range') else None

            if date_range is not None:
                date_range = json.loads(date_range)
                startDate_str = date_range['start_date']
                endDate_str = date_range['end_date']
                start_datetime = datetime.strptime(startDate_str, "%Y-%m-%d").date()
                end_datetime = datetime.strptime(endDate_str, "%Y-%m-%d").date()

            allSales = Sale.objects.all().order_by('-created_at')
            if client_name is not None:
                allSales = allSales.filter(lead__client_name__icontains=client_name,is_deleted=False).order_by('-created_at')

            if contact_no is not None:
                allSales = allSales.filter(lead__contact_no__icontains=contact_no,is_deleted=False).order_by('-created_at') 
                
            if date_range is not None: 
                allSales = allSales.filter(created_at__date__gte=start_datetime,created_at__date__lte=end_datetime,is_deleted=False).order_by('-created_at') 
                
            if client_name is not None and contact_no is not None:
                allSales = allSales.filter(Q(lead__client_name__icontains=client_name) | Q(contact_no__icontains=contact_no),is_deleted=False).order_by('-created_at')
            
            all_sales_contact_no = [obj.lead.contact_no for obj in allSales]
            related_users = Users.objects.filter(contact_no__in=all_sales_contact_no)
            model2_dict = {}
            for obj in related_users:
                if obj.contact_no not in model2_dict:
                    model2_dict[obj.contact_no] = []
                model2_dict[obj.contact_no].append(obj)

            for obj in allSales:
                contact_no = obj.lead.contact_no
                if contact_no in model2_dict:
                    obj.related_users = model2_dict[contact_no]
                else:
                    obj.related_users = []
            noOfRecords = 15
            p = Paginator(allSales, noOfRecords)
            page_obj = p.get_page(pageNo)
            
            try:
                page_obj = p.page(pageNo)
            except PageNotAnInteger:
                page_obj = p.page(1)
            except EmptyPage:
                page_obj = p.page(p.num_pages)
            
            new_data = []
            for sale in page_obj:
                model1_data = {
                'id':sale.pk,
                'name':sale.lead.client_name,
                'email':sale.lead.email,
                'conact_no':sale.lead.contact_no,
                'source':{
                    'id':sale.lead.source.pk,
                    'name':sale.lead.source.name
                },
                'requirement':sale.lead.requirement,
                'follow_date':datetime.strftime(sale.follow_date,"%Y-%m-%dT%H:%M") if sale.follow_date else "",
                'status':sale.sale_status,
                'remark':sale.remark,
                'temp_data':sale.temp_data,
                'created_at':sale.created_at
                }

                related_users_data = []
                for related_obj in sale.related_users:
                    related_user_data = {
                        'role': related_obj.role.name,
                        'designation': related_obj.designation,
                    }
                    related_users_data.append(related_user_data)

                model1_data['related_users'] = related_users_data
                new_data.append(model1_data)
            sale_data = new_data
            sales_count = Sale.objects.all().count()
            follow_count=Sale.objects.filter(follow_date__isnull=False).count()
            
            data = {
                "total_sales":sales_count,
                "follow_count":follow_count,
                "total_pages":p.num_pages
            }

        except allSales.DoesNotExist:
            return JsonResponse({'message':"No data found for sales"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'res_data':sale_data, "data":data}, status=status.HTTP_200_OK)
    
    def put(self,request):
        try:
            sale_id=request.data.get('id')
            upd_sale=Sale.objects.get(pk=sale_id)
            follow_date_str = None
            follow_date = None
            
            user_instance=request.user
            if user_instance.role.name == "admin" or user_instance.role.name == "sales":
                if request.data.get('follow_date'):
                    follow_date_str= request.data.get('follow_date')
                    follow_date=datetime.strptime(follow_date_str,"%Y-%m-%dT%H:%M")

                with transaction.atomic():
                    upd_sale.sale_status=request.data.get('status') if request.data.get('status') else None
                    upd_sale.remark=request.data.get('remark') if request.data.get('remark') else None
                    upd_sale.follow_date=follow_date
                    upd_sale.save()         
            else:
                return JsonResponse({"message":"Sorry! You can not edit the sale"},status=status.HTTP_401_UNAUTHORIZED)
                                      
        except Exception as e:
            return JsonResponse({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
        return JsonResponse({"message":"Sale Updated Successfully"},status=status.HTTP_200_OK)
        
        
    def delete(self, request):
        id = request.GET.get('id')
        if not id:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_instance=request.user
            if user_instance.role.name == "admin" or user_instance.role.name == "sales":
                with transaction.atomic():
                    deleteSale = Sale.objects.get(pk=id)
                    deleteSale.lead.is_assigned=False
                    deleteSale.lead.save()
                    deleteSale.delete()
                    return JsonResponse({'message':'Sale deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
               return JsonResponse({"message":"Sorry! You can not delete the sale"},status=status.HTTP_401_UNAUTHORIZED) 
        except IntegrityError as i:
            return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
    
class getAllSaleEmployees(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            user_instance=Users.objects.filter(role__name="sales",is_deleted=False).order_by('name')
            employee_data=[
                {
                    'id':user.pk,
                    'name':user.name
                } for user in user_instance ]
                
        except Exception as e:
            return JsonResponse({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'employee_data':employee_data},status=status.HTTP_200_OK)
    
class clientTemplateView(CsrfExemptMixin,APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request):
        try:
            data=request.data.get("data")
            sale_instance=Sale.objects.get(lead__email=request.user)
            
            with transaction.atomic():
                sale_instance.temp_data=data
                sale_instance.save()
            
        except Sale.DoesNotExist:
            return JsonResponse({"message":"Sale with this user does not exist"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"Requirements Submitted"},status=status.HTTP_200_OK)
        
