from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
import random
from .models import User
import uuid
from rest_framework.authtoken.models import Token


def generate_verification_code():
    return random.randint(100000, 999999)


def check_phone_num(phone_num):
    return True

class login(View):
    def post(self, request):
        kwargs: dict = json.loads(request.body)
        try:
            session_verification_code = request.session.get("verification_code")
            user_code = kwargs.get("verification_code")
            if session_verification_code != user_code:
                return JsonResponse({"status": "error", "message": "Invalid verification code"})
            phone_num = kwargs.get("phone_num")
            user = User.objects.get(phoneNumber=phone_num)
            if user is None:
                user_uuid = str(uuid.uuid4())
                user_name = "user" + user_uuid
                user = User.objects.create(phoneNumber=phone_num, is_admin_or_not=False, user_name=user_name)
                user.save()
            request.session["user_id"] = user.user_id
            token = Token.objects.create(user=user)
            print(f"token:{token.key}")
            return JsonResponse({"status": "success", "message": "Login successful","token": token.key})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


class send_verification_code(View):
    def post(self, request):
        kwargs: dict = json.loads(request.body)
        try:
            phone_num = kwargs.get("phone_num")
            if check_phone_num(phone_num) == False:
                return JsonResponse({"status": "error", "message": "Invalid phone number"})
            code = generate_verification_code()
            print(f"code:{code}")
            request.session["verification_code"] = code
            return JsonResponse({"status": "success", "message": "Verification code sent"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

        