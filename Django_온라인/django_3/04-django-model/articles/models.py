from django.db import models

# Create your models here.
# models라는 모듈의 Model이라는 클래스 상속
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
