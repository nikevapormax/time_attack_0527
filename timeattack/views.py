# render 함수를 통해서 html을 화면에 띄워준다.
from django.shortcuts import render, redirect
# 나와 동일한 위치에 있는 모델 중에서 UserModel을 가져와 사용하겠다.
from .models import UserModel
from django.contrib.auth import get_user_model


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        new_user = UserModel()
        if email.include('@'):
            new_user.email = email
        if len(password) >= 8:
            new_user.password = password

        new_user.save()

        # 위와 같이 회원정보를 성공적으로 저장하게 되면 로그인 페이지로 리다이렉트해준다.
        return redirect('/')