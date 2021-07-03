from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    quiz1 = request.GET['quiz1']
    quiz2 = request.GET['quiz2']
    count = 0
    if(quiz1 == '눈썹'):
        count +=1
    if(quiz2 == '목란'):
        count +=1
    return render(request, 'result.html', {'quiz1':quiz1, 'quiz2':quiz2, 'count':count})