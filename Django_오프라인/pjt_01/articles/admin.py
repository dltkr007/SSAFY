from django.contrib import admin

# Register your models here.

# migratin 오류 해결
# models.py에서 post 클래스에 접근하겠다.
from .models import Post
# admin.py에 post를 저장하겠다
admin.site.register(Post)