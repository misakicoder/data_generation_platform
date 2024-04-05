from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
import logging
from .models import Task
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
            return JsonResponse({"status": "success", "message": "Task post successful","task":model_to_dict(now_task)})
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