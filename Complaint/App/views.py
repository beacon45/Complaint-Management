from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#It doesn't directly gives access to the user they had to login then will be directed
@login_required(login_url='login')
def IndexPage(req):
    return render(req,'index.html')

def LoginPage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        pass1=req.POST.get('pass')
        user=authenticate(req,username=username,password=pass1)
        if user is not None:
            login(req,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(req,'login.html')

def LogoutPage(req):
    logout(req)
    return redirect('login')

def RegistrationPage(req):
    if req.method=='POST':
        uname=req.POST.get('username')
        email=req.POST.get('email')
        pass1=req.POST.get('password1')
        pass2=req.POST.get('password2')
        role=req.POST.get('role')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            myUser=User.objects.create_user(uname,email,pass1)
            myUser.save()
            return redirect('login')
    return render(req,'registration.html')