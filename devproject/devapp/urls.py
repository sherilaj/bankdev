
from django.urls import path

from devapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('loginnew',views.loginnew,name='loginnew'),
    path('userform',views.userform,name='userform'),
    path('lastform',views.lastform,name='lastform')
]
