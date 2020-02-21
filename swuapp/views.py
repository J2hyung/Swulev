from django.shortcuts import render, get_object_or_404
from .models import User 

# Create your views here.

def login(request):
    user1 = User.objects.all
    return render(request, 'login.html', {'user1':user1})

def main(request):

    return render(request, 'main.html')

def detail(request):

    return render(request, 'detail.html')

def mypage(request):
    return render(request, 'mypage.html')