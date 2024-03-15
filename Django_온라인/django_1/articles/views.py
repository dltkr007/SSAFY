from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request):
    #render : 요청받은 페이지 결과물을 리턴하는 함수
    #render(요청 객체, #templates 폴더 이후의 경로)
    return render(request, 'index.html')
