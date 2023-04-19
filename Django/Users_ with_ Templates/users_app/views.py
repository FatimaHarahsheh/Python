from django.shortcuts import render,HttpResponse,redirect
from .models import users
def index(request):
    context={
        'allusers':users.objects.all()
    }
    return render(request, "index.html" , context)
def adduser(request):
    if request.method=='POST' :
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        age=request.POST['age']
        adduser=users(first_name=fname,last_name=lname,age=age,email_addres=email)
        adduser.save()
    return redirect("/")
# Create your views here.
