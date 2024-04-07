from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from Task.models import Task
from User.models import User
from .models import Data
from util.ossUtil import ossUtil
import json
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class data(View):
    def post(self, request):
        kwargs:dict = json.loads(request.POST.get("body")) 
        try:
            file = request.FILES.get("file")
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            data_type = kwargs.get("data_type")
            task_type = kwargs.get("task_type")
            date_description = kwargs.get("data_description")
            ori_data_url = ossUtil.upload(task_type +"/", date_description, file)
            user = User.objects.get(user_id=user_id)
            now_data = Data.objects.create(
                data_type=data_type,
                data_description=date_description,
                ori_data_url=ori_data_url,
                task_type=task_type,
                user_id=user,
            )
            return JsonResponse({"status": "success", "message": "Data post successful"})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)}) 


class ori_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            ori_datas = Data.objects.filter(user_id=user_id,task_type=task_type).values()
            return JsonResponse({"status": "success", "message": "Get ori data successful", "ori_datas": list(ori_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})


class cleaned_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            cleaned_datas = Data.objects.filter(user_id=user_id,task_type=task_type).exclude(cleaned_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get cleaned data successful", "cleaned_datas": list(cleaned_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class marked_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            marked_datas = Data.objects.filter(user_id=user_id,task_type=task_type).exclude(marked_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get marked data successful", "marked_datas": list(marked_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class preprocessed_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            preprocessed_datas = Data.objects.filter(user_id=user_id,task_type=task_type).exclude(preprocessed_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get preprocessed data successful", "preprocessed_datas": list(preprocessed_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class marked_preprocessed_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            marked_preprocessed_datas = Data.objects.filter(user_id=user_id,task_type=task_type).exclude(marked_preprocessed_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get marked preprocessed data successful", "marked_preprocessed_datas": list(marked_preprocessed_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})