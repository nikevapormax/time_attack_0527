# timeattack/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up_view, name='sign-up'),
]
