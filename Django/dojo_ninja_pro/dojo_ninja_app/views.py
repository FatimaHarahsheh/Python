from django.shortcuts import redirect, render,HttpResponse
from .models  import Dojo ,Ninja

def index(request):
    context = {
        'x' : Dojo.objects.all()
        } 
       
    
    
    return render(request,'index.html')
def turnin(request):
    name=request.POST['name']
    city=request.POST['city']
    state=request.POST['state']
    Dojo.objects.create(name=name,city=city,state=state)
    return redirect('/')

def display(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dojo=request.POST['dojo']
    Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=dojo)
    return redirect('/')


# Create your views here.
