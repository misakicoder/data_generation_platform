import threading
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from User import User  # 你的 User 模型的实际导入路径

_thread_locals = threading.local()

def get_current_user():
    return getattr(_thread_locals, 'user', AnonymousUser())

class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            user = User.objects.filter(token=token).first()
            if user:
                _thread_locals.user = user
                request.user = user
            else:
                _thread_locals.user = AnonymousUser()
                request.user = SimpleLazyObject(lambda: get_current_user())
        else:
            _thread_locals.user = AnonymousUser()
            request.user = SimpleLazyObject(lambda: get_current_user())

    def process_response(self, request, response):
        # 这个方法在视图函数处理请求之后被调用
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return response