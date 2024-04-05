from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from Task.models import Task
from User.models import User
from .models import Data
import json
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class data(View):
    def post(self, request):
        kwargs:dict = json.loads(request.POST.get("body")) 
        try:
            file = request.FILES.get("file")
            # with open('123.csv', "wb") as f:
            #     f.write(file.read())
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            data_type = kwargs.get("data_type")
            date_description = kwargs.get("data_description")
            ori_data_url = "123"
            task_id = kwargs.get("task_id")
            task = Task.objects.get(task_id=task_id)
            user = User.objects.get(user_id=user_id)
            now_data = Data.objects.create(
                data_type=data_type,
                data_description=date_description,
                ori_data_url=ori_data_url,
                task_id=task,
                user_id=user,
            )
            return JsonResponse({"status": "success", "message": "Data post successful"})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)}) 