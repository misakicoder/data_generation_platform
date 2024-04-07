from django.shortcuts import render
from Task.models import Task
from django.http import JsonResponse
from django.views import View
from .models import Model
import json
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class models(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_id = request.GET.get("task_id")
            data_type = request.GET.get("data_type")
            task = Task.objects.get(task_id=task_id)
            models = Model.objects.filter(task_type=task.task_type,algorithm_name=task.task_algorithm,data_type=data_type).values()
            return JsonResponse({"status": "success", "message": "Get model list successful", "models": list(models)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})