from django.contrib import admin
from django.urls import path
# 명시적 상대 경로 'from .' = 현재 위치 -> 없어도 되지만 명시적으로 붙임
from . import views

app_name = 'pages'
urlpatterns = [
# /articles/~~/ 형식으로 변함
    # path('index/', views.index),


]
