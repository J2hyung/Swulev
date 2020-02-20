from django.shortcuts import render, get_object_or_404

# Create your views here.

def login(request):

    return render(request, 'login.html')

def main(request):

    return render(request, 'main.html')

def detail(request):

    return render(request, 'detail.html')

def mypage(request):
    return render(request, 'mypage.html')