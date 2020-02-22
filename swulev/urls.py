from django.contrib import admin
from django.urls import path
from swuapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('signup', signup, name='signup'),
    path('main/', main, name='main'),
    path('detail/', detail, name='detail'),
    path('mypage/', mypage, name='mypage'),
]
