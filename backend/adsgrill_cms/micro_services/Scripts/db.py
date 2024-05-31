import sys
from app.models import Sale, Users
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db import transaction
import pandas as pd

class MasterUpdate(APIView):
    def post(self, request):
        arr = []
        try:
            df = pd.read_csv('C:/Ads-Grill-CRM/backend/adsgrill_cms/micro_services/Scripts/sale_data.csv')
            df2 = df.fillna(value='')
            df3 = df2.values.tolist()
            print(df2)
            for row in df3:
                created_at, updated_at, is_deleted, assignee, lead_id, status_id, follow_date, remark, sale_status, temp_data, row_col = row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]
                with transaction.atomic():
                    sale_instance = Sale.objects.create(
                        created_at=str(created_at) if created_at else None,
                        updated_at=str(updated_at) if updated_at else None,
                        is_deleted=is_deleted,
                        lead_id=lead_id,
                        status_id=status_id if status_id else None,
                        follow_date=str(follow_date) if follow_date else None,
                        remark=remark if remark else None,
                        sale_status=sale_status if sale_status else None,
                        temp_data=temp_data if temp_data else None,
                        row_color=row_col if row_col else None,
                        is_assigned=True
                    )

                    if assignee:
                        assignee = Users.objects.get(pk=assignee)
                        sale_instance.assignee.add(assignee)
                    print(sale_instance)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"Error retrieving data: {e}")
        return JsonResponse({"message": "Data restore successfully"})

