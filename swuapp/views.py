from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture
from .models import User
# Create your views here.

def login(request):
    #user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    if request.method == 'POST':
            userid = request.POST['userid']
            userpw = request.POST['userpw']
            user = auth.authenticate(request, userid=userid, userpw=userpw)
            if user is not None:
                auth.login(request, user)
                return redirect('login')
            else:
                return render(request, 'login.html', {'error': 'ID 또는 PW가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')
    # user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    # return render(request, 'login.html', {'user1':user1})

def main(request):
    mylecture_list = Lecture.objects.filter(lectureid__startswith="VD04013")
    return render(request, 'main.html', {"mylecture_list": mylecture_list})

def detail(request):

    return render(request, 'detail.html')

def mypage(request):
    return render(request, 'mypage.html')