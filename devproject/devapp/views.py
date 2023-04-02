from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method =='POST':

        u1=request.POST['username']
        p1=request.POST['password']
        c1=request.POST['cpassword']
        if p1==c1:
            if User.objects.filter(username=u1).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=u1,password=p1)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('loginnew')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def loginnew(request):
    return render(request,'loginnew.html')
def userform(request):
    return render(request,'userform.html')
def lastform(request):
    return render(request,'lastform.html')