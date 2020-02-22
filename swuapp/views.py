from django.shortcuts import render, get_object_or_404, redirect
#from .models import Lecture
from .models import User
# Create your views here.

def login(request):
    #user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    user_data = User(
            userid = "dd" ,
            userpw = "dd")
    user_data.save()
            # 새 객체 INSERT
        
    return render(request, 'login.html',{'user_data':user_data})

def main(request):
    return render(request, 'main.html')

def detail(request):

    return render(request, 'detail.html')

def mypage(request):
    return render(request, 'mypage.html')