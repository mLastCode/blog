from django.shortcuts import render
from django.views import View
# Create your views here.

from django.http.response import HttpResponseBadRequest, HttpResponse
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection

# 注册视图
class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')


# 图片验证码视图
class ImageCodeView(View):

    def get(self, request):

        uuid = request.GET.get('uuid')

        if uuid is None:
            return HttpResponseBadRequest("请求参数错误")

        text, image = captcha.generate_captcha()

        redis_conn = get_redis_connection('default')
        redis_conn.setex = ('img: %s' % uuid, 300, text)

        return HttpResponse(image, content_type='image/jpg')
