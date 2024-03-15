from django.shortcuts import render

# Create your views here.
# request 요청 : 클라이언트에서 서버로 보내는 요청
def index(request):
    return render(request, './articles/index.html')
