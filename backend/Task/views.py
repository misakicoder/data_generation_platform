from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
import logging
from .models import Task
from .models import DataManager
from datetime import datetime
import json
from User.models import User


logger = logging.getLogger(__name__)


# Create your views here.
class tasks(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            tasks = Task.objects.filter(user_id=user_id).values()
            return JsonResponse({"status": "success", "message": "Task get successful","tasks":list(tasks)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})


class task(View):
    def get (self, request):
        try:
            task_id = request.GET.get("task_id")
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task = Task.objects.get(task_id=task_id, user_id=user_id)
            return JsonResponse({"status": "success", "message": "Task get successful","task":model_to_dict(task)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

    def post(self, request):
        kwargs: dict = json.loads(request.body)
        try:
            task_type = kwargs.get("task_type")
            user_id = request.session.get("user_id")
            user = User.objects.filter(user_id=user_id).first()
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            now_task = Task.objects.create(
                task_type=task_type, 
                user_id=user,
                task_state="pending",
                task_name=task_type +"\n"+datetime.now().strftime("%Y%m%d%H%M%S"),
            )
            now_data_manager=DataManager.objects.create(
                task_id=now_task
            )
            return JsonResponse({"status": "success", "message": "Task post successful","task":model_to_dict(now_task),"data_manager":model_to_dict(now_data_manager)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

    def delete(self,request):
        kwargs: dict = json.loads(request.body)
        try:
            task_id = kwargs.get("task_id")
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task = Task.objects.get(task_id=task_id, user_id=user_id)
            task.delete()
            return JsonResponse({"status": "success", "message": "Task delete successful"})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})


class data_manager(View):
    def get(self, request):
        try:
            task_id = request.GET.get("task_id")
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            data_manager = DataManager.objects.get(task_id=task_id)
            return JsonResponse({"status": "success", "message": "Data manager get successful","data_manager":model_to_dict(data_manager)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

    def post(self, request):
        kwargs: dict = json.loads(request.body)
        try:
            task_id = kwargs.get("task_id")
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            data_manager = DataManager.objects.get(task_id=task_id)
            task = Task.objects.get(task_id=task_id)
            task.task_algorithm = kwargs.get("task_algorithm")
            task.save()
            data_manager.data_clean = kwargs.get("data_clean")
            data_manager.data_mark = kwargs.get("data_mark")
            data_manager.data_preprocess = kwargs.get("data_preprocess")
            data_manager.data_generate = kwargs.get("data_generate")
            data_manager.save()
            return JsonResponse({"status": "success", "message": "Data manager post successful","data_manager":model_to_dict(data_manager)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})