from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

from .models import Catlist
from .models import Catphoto
from .forms import CatlistPost
from .forms import Catupdate

def map_skku(request):
    
    cats = Catlist.objects.all()
    return render(request, 'map_skku.html', {'cats' : cats } )

def each_cat(request, key):
    all_cats = Catlist.objects
    each_cat = get_object_or_404(Catlist, pk = key)
    
    pos_y = each_cat.pos_y
    pos_x = each_cat.pos_x
    
    pos_ylist = pos_y.split()
    pos_xlist = pos_x.split()
    list_len = len(pos_ylist)
        
    matrix = []

    for i in range(list_len):
        line = []              
        for j in range(2):
            line.append(0)     
        matrix.append(line)         
             
    
    for i in range( list_len ) :
        matrix[i][0] = float(pos_ylist[i])

    for j in range( list_len ) :
        matrix[j][1] = float(pos_xlist[j])
 
    print(matrix)        
            
    
    return render(request, 'each_cat.html', {'all_cats': all_cats, 'each_cat' : each_cat , 'matrix' : matrix ,
                                            'len' : list_len   } )


def new(request):
    if request.method == 'POST' :
        cat = Catlist()
        cat.name = str(request.POST['name'])
        cat.age = str(request.POST['age'])
        cat.gender = str(request.POST['gender'])
        cat.info = str(request.POST['info'])
        cat.catimage = request.FILES['catimage']
        some_var = request.POST.getlist('feature[]')

        if 'furious' in some_var:
            cat.furious = True
        else:
            cat.furious = False
        if 'food' in some_var:
            cat.food = True
        else:
            cat.food = False
        if 'health' in some_var:
            cat.health = True
        else:
            cat.health = False
        if 'family' in some_var:
            cat.family = True
        else:
            cat.family = False
        if 'touch' in some_var:
            cat.touch = True
        else:
            cat.touch = False
        
        # marks = request.POST.getlist('feature')
        # # print(marks)
        # for mark in marks :
        #     cat.marks += mark
        
        # print(cat.marks)
        
        cat.pos_y = str( request.POST['pos_y'] )
        cat.pos_x = str( request.POST['pos_x'] )
        
        print(cat.pos_y)
        print(cat.pos_x)

        cat.save()
        return redirect('map_skku')
    else:

        return render(request, 'new.html')

    

def detail_cat(request, key):
    if request.method == 'POST':
        newphoto = Catphoto()
        newphoto.title = request.POST['description']
        newphoto.photo = request.FILES['photo']
        newphoto.pub_date =  timezone.datetime.now()
        newphoto.catnum = key
        newphoto.save()
        return redirect('detail_cat', key)
    else:
        photos = Catphoto.objects
        this_cat = get_object_or_404(Catlist, pk = key)
    
        return render(request, 'detail_cat.html' ,{ 'c' : this_cat , 'photos' : photos })


def delete(request, key):
    delete_cat = get_object_or_404(Catlist, pk = key)
    delete_cat.delete()
    
    return redirect('map_skku')
    
def delete2(request, key):
    delete_photo = get_object_or_404(Catphoto, pk = key)
    catnumber= delete_photo.catnum
    delete_photo.delete()
    
    return redirect('detail_cat', catnumber)




def update(request, key) :
    changewhat = get_object_or_404(Catlist, pk = key)
    cat = Catupdate(request.POST, request.FILES, instance = changewhat)
    
    if request.method == 'POST' :
     
        if 'furious' in some_var:
            cat.furious = True
        else:
            cat.furious = False
        if 'food' in some_var:
            cat.food = True
        else:
            cat.food = False
        if 'health' in some_var:
            cat.health = True
        else:
            cat.health = False
        if 'family' in some_var:
            cat.family = True
        else:
            cat.family = False
        if 'touch' in some_var:
            cat.touch = True
        else:
            cat.touch = False

        cat.pos_y = str( request.POST['pos_y'] )
        cat.pos_x = str( request.POST['pos_x'] )       
        cat.save()

        return redirect('each_cat', key)

    else :
        
        pos_y = cat.pos_y
        pos_x = cat.pos_x

        pos_ylist = pos_y.split()
        pos_xlist = pos_x.split()
        list_len = len(pos_ylist)

        matrix = []

        for i in range(list_len):
            line = []              
            for j in range(2):
                line.append(0)     
            matrix.append(line)         


        for i in range( list_len ) :
            matrix[i][0] = float(pos_ylist[i])

        for j in range( list_len ) :
            matrix[j][1] = float(pos_xlist[j])

        print(matrix)        
            
    
        
        return render(request, 'update.html', { 'cat' : cat, 'matrix' : matrix , 'len' : list_len } )
    

    
    
    