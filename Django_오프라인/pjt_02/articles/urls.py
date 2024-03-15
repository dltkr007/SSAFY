from django.contrib import admin
from django.urls import path, include
# from articles import views
from . import views

app_name = 'articles'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('articles/', include('articles.urls')),
    path('index/', views.index, name = "index"),
    path('dinner/', views.dinner, name = "dinner"),
    path('search/', views.search, name = "search"),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
    path('articles/<int:num>/', views.detail, name = 'detail'),
    
]
