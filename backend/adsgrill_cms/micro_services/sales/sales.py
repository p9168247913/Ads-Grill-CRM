from app.models import Users
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

class SalesView(APIView):
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
        
