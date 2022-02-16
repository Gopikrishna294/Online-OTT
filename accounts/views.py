from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here
def registration(req):
    
    if req.method=='POST':
        userform = MyUserCreationForm(req.POST)
        if userform.is_valid():
            userform.save()
            messages.success(req,'Account Successfully Created')
            return redirect('login')
    else:# if request is not POST (i.e GET)
        userform = MyUserCreationForm()
    data = {'userform':userform}
    return render(req,'accounts/registration.html',data)
    
def mylogin(req):
    if req.method=='POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:

            login(req,user)
            messages.success(req,'Login Successfully....')
            return redirect('Home')
        else:
            messages.error(req,'Invalid Username and password....')
            return redirect('login')
    elif req.method=='GET':
        loginform = AuthenticationForm()
        data ={'loginform':loginform}
        return render(req,'accounts/login.html',data)

def mylogout(req):
    req.user=None
    logout(req)
    #messages.success(req,'Logout Successfully....')
    return redirect('login')