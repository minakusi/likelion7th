from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':    
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)  
        if user is not None:
            auth.login(request, user)
            return redirect('map_skku')
        else:
            return render(request, 'login.html', {'error': '아이디 or 패스워드가 맞지 않는다냥'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'signup.html', {'already': '이미 가입됐다냥'})
            else:
                user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('login')
    return render(request, 'signup.html')
    
    
def logout(request) :
    if request.method =="POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'home.html')