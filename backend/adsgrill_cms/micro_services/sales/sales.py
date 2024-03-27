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

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple
class SalesView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        try:
            lead_ids=request.data.get('lead_ids').split(',')
            lead_ids = [int(lead_id) for lead_id in lead_ids]
            assignee_id=request.data.get('assignee_id')
            assignee_instance=Users.objects.get(pk=assignee_id)
            
            leads=Lead.objects.filter(pk__in=lead_ids)
            
            with transaction.atomic():
                sales_instance= [Sale(
                    lead=lead_id,
                    assignee=assignee_instance
                )for lead_id in leads]
                
                Sale.objects.bulk_create(sales_instance)
                
            return JsonResponse({'message':f"leads assigned successfully to {assignee_instance.name}"},status=status.HTTP_201_CREATED)
        
        except IntegrityError as i:
            return JsonResponse({"message":str(i)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return JsonResponse({"message":str(e)})
    
    def get(self, request):
        try:
            sales_Man = Users.objects.filter(role__name = 'sales', designation = 'sales_manager').order_by('-created_at')
            data = [{
                'id':man.pk,
                'name':man.name
            }for man in sales_Man]

        except sales_Man.DoesNotExist:
            return JsonResponse({'message':"Sales Manager Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'res_data':data}, status=status.HTTP_200_OK)
    
    def put(self,request):
        try:
            sale_id=request.data.get('sale_id')
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
    
class getAllSaleEmployees(APIView):
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
        
