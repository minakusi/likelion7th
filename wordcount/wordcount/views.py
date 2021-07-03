from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    dic = {}
    thanos = ''
    for i in range(int(len(text)/2)):
        thanos += text[i]
    spidy=thanos.split()
    for word in spidy:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':dic.items(), 'balance':thanos})