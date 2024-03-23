import threading
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from User import User  # 你的 User 模型的实际导入路径

public_path = [
    '/login/',
    '/verify_code/',
]

_thread_locals = threading.local()

def get_current_user():
    return getattr(_thread_locals, 'user', AnonymousUser())

class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in public_path:
            pass

        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.get(user_id=user_id)
            if user.exists():
                _thread_locals.user_id = user.user_id
            else:
                return JsonResponse({'error': 'Authentication required'}, status=401)
        else:
            return JsonResponse({'error': 'Authentication required'}, status=401)

    def process_response(self, request, response):
        return response