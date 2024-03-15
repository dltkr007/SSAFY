from django.contrib import admin
from django.urls import path, include
# from articles import views
from . import views

app_name = 'pages'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('articles/', include('articles.urls')),
    path('index/', views.index, name='index'),
         
]
