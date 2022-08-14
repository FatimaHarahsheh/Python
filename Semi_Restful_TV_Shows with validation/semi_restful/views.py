from django.shortcuts import redirect, render 
from django.contrib import messages
from .models import *
def index(request):
    context={
        'sho':show.objects.all()
        
    }
    return render(request,'index.html',context)
    
def addshow(request):
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['date']
        description=request.POST['description']

        show.objects.create(title=title,network=network,release_date=release_date,description=description)
        return redirect('/')

def anythings(request):
        return redirect('/shows')


def diplay(request):
        return render(request,'add.html')
def things(request,id):
    v=id
    context={
        'va':show.objects.get(id=v)
    

    }
    return render(request,'edit.html',context)
def new(request,id):
    updat=show.objects.get(id=id)
    updat.title=request.POST['title']
    updat.network=request.POST['network']
    updat.release_date= request.POST['date']
    updat.description=request.POST['description']
    updat.save()

    return redirect('/shows')

def allinfo(request,id):
    context={
        'infor': show.objects.get(id=id)
    }

    return render (request,'shows.html',context)

def destroy(request,id):
    dest =show.objects.get(id=id)
    

    dest.delete()
    return redirect('/')



