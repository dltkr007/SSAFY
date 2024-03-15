from django.db import models

# Create your models here.

# models.Model : 데이터베이스(DB)의 테이블 구성
class Post(models.Model):
    # 제목은 문자로 만들건데 최대 길이 제한은 100으로 하겠다
    title = models.CharField(max_length = 100)
    # 컨텐츠는 글자 제한 없다
    content = models.TextField()
    # 생성된 날짜는 자동으로 생성하겠다
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        # 게시글을 생성할 때 pk(id : 고유 번호), title로 구성
        return f'[{self.pk} {self.title}]'
    # 마이그레이션은 데이터베이스 스키마를 관리하고 업데이트하는 과정
    # -> 데이터베이스 모델이 변경되거나 새로운 모델이 추가될 때, 변겅 사항을 DB에 적용
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py createsuperuser 관리자 계정