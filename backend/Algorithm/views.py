from django.shortcuts import render
from .models import Algorithm
from django.http import JsonResponse
from django.views import View
import json
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class algorithms(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            algorithms = Algorithm.objects.filter(task_type=task_type).values()
            return JsonResponse({"status": "success", "message": "Get algorithm list successful", "algorithm_list": list(algorithms)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})