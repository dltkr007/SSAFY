from django.shortcuts import render
import random
# Create your views here.

def index(request):
    context = {
        'name' : 'jane',
        'num' : 1
    }
    # render 함수의 3번째 항목에는 매개 변수가 들어감
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['족발', '보쌈', '치킨', '피자']
    picked = random.choice(foods)

    context = {
        'foods' : foods,
        'picked' : picked,

    }

    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)

# articles/articles/1 --> 1이라는 값이 num에 전달되어 함수 안에서 사용
def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)

