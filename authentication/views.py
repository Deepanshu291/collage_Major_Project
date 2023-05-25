from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def login(req):
    # return HttpResponse('this is login')
    if req.method == 'POST':
        username = req.POST['uname']
        password = req.POST['pswd']
        
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(req,user)
                return redirect(to="home")
            messages.error(req,"Incorrect Username and Password")
            return redirect(to="login") 
    # if user is not None: 
    messages.info(req, 'Please fill username and password')
    return render(req, 'login.html')

def logout(req):
    auth.logout(req)
    return redirect(to='login')