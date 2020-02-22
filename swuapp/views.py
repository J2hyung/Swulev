from django.shortcuts import render, get_object_or_404, redirect
#from .models import Lecture
from .models import User
# Create your views here.

def signup(request):
    #user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    if request.method == 'POST':
            user_id = request.POST['id']
            user_pw = request.POST['passwd']
            user = User(userid=user_id, userpw=user_pw)
            user.save()
            if user is not None:
                return redirect('main')
            else:
                return render(request, 'signup.html', {'error': 'ID 또는 PW가 올바르지 않습니다.'})
    else:
        return render(request, 'signup.html')
    # user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    # return render(request, 'login.html', {'user1':user1})

def login(request):
    #user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    if request.method == 'POST':
            user_id = request.POST['id']
            user_pw = request.POST['passwd']
            if user_id is not None:
                return redirect('main')
            else:
                return render(request, 'login.html', {'error': 'ID 또는 PW가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')
    # user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    # return render(request, 'login.html', {'user1':user1})

def main(request):
    return render(request, 'main.html')

def detail(request):

    return render(request, 'detail.html')

def mypage(request):
    return render(request, 'mypage.html')