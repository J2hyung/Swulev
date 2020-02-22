from django.shortcuts import render, get_object_or_404, redirect
#from .models import Lecture
from .models import *
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
    mylecture_list = Lecture.objects.filter(lectureid__startswith="VD04013")
    return render(request, 'main.html', {"mylecture_list": mylecture_list})

def detail(request, current_lectureid):

    current_lecture = get_object_or_404(Lecture, lectureid=current_lectureid)
    boards = Board.objects.filter(b_lectureid = current_lectureid)

    return render(request, 'detail.html', {'current_lecture' : current_lecture, 'boards': boards})

def mypage(request):
    return render(request, 'mypage.html')