from django.shortcuts import redirect, render,HttpResponse
from .models import *
def index(request):
    context={
        'bo' : book.objects.all()
    }
    return render(request,"index.html",context)


def add_book(request):
    ti = request.POST['title']
    desc = request.POST['descripition']
    bo = create_book(ti,desc)

    return redirect('/')

def add_author(request):
    fname = request.POST["first"] 
    lname = request.POST["last"]
    note = request.POST["note"]
    aut = authors.objects.create(first_name= fname,last_name= lname,notes = note)
    return redirect('/')

def deti(request,id):
    context={
        'bo' : book.objects.get(id=id),
        'au' : authors.objects.all()
    }
    return render(request,'books.html',context)


def author(request):
    context={
        'au' : authors.objects.all()
    }
    return render(request,'authhors.html',context)

def author_id(request):
    context={
        'bo' : book.objects.get(id=id),
        'au' : authors.objects.all()
    }
    return render(request,'authors_det.html',context)


def bookjoin(request):
    ba = request.POST['x.id']
    au=book.objects.all()
    au.bkat=ba
    return redirect('books/id')





