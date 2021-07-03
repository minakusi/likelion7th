from django.shortcuts import render

# Create your views here.


def about_1(request):  
    return render(request, 'about_1.html')

def about_2(request):
    return render(request, 'about_2.html')

def home(request):
    return render(request, 'home.html')