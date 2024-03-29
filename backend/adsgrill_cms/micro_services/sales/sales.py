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
            
            with transaction.atomic():
                sales_instance= [Sale(
                    lead=lead_id,
                    assignee=assignee_instance
                )for lead_id in leads]

                for lead in leads:
                    lead.is_assigned = True
                    lead.save()
                
                Sale.objects.bulk_create(sales_instance)
                
            return JsonResponse({'message':f"leads assigned successfully to {assignee_instance.name}"},status=status.HTTP_201_CREATED)
        
        except IntegrityError as i:
            return JsonResponse({"message":str(i)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return JsonResponse({"message":str(e)})
    
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
            noOfRecords = 15
            p = Paginator(allSales, noOfRecords)
            page_obj = p.get_page(pageNo)
            
            try:
                page_obj = p.page(pageNo)
            except PageNotAnInteger:
                page_obj = p.page(1)
            except EmptyPage:
                page_obj = p.page(p.num_pages)
            sale_data = [{
                'id':sale.pk,
                'name':sale.lead.client_name,
                'email':sale.lead.email,
                'conact_no':sale.lead.contact_no,
                'source':{
                    'id':sale.lead.source.pk,
                    'name':sale.lead.source.name
                },
                'requirement':sale.lead.requirement,
                'created_at':sale.created_at

            }for sale in page_obj]

            sales_count = Sale.objects.all().count()
            data = {
                "total_sales":sales_count,
                "total_pages":p.num_pages
            }

        except allSales.DoesNotExist:
            return JsonResponse({'message':"No data found for sales"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"message":str(e)})
        return JsonResponse({'res_data':sale_data, "data":data}, status=status.HTTP_200_OK)
    
    def put(self,request):
        try:
            sale_id=request.data.get('id')
            upd_sale=Sale.objects.get(pk=sale_id)
            follow_date_str = None
            follow_date = None
            if request.data.get('follow_date'):
                follow_date_str= request.data.get('follow_date')
                follow_date=datetime.strptime(follow_date_str,"%Y-%m-%dT%H:%M:%S")
            
            with transaction.atomic():
                upd_sale.sale_status=request.data.get('status') if request.data.get('status') else None
                upd_sale.remark=request.data.get('remark') if request.data.get('remark') else None
                upd_sale.follow_date=follow_date
                upd_sale.save()
                
            return JsonResponse({"message":"Lead Updated Successfully"},status=status.HTTP_200_OK)
            
        except Exception as e:
            return JsonResponse({"message":str(e)})
        
    def delete(self, request):
        id = request.GET.get('id')
        if not id:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                deleteSale = Sale.objects.get(pk=id)
                deleteSale.delete()
                return JsonResponse({'message':'Sale deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
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
            return JsonResponse({"message":str(e)})
        return JsonResponse({'employee_data':employee_data},status=status.HTTP_200_OK)
        
