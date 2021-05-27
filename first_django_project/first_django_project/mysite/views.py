from django.shortcuts import render, HttpResponse,redirect
from django.http  import  JsonResponse 
def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def create(request):
    return redirect("/blogs")
def show(request ,number):
    return  HttpResponse(f"placeholder to display blog number: {number}")
def edit(request ,number):
    return HttpResponse (f"placeholder to edit blog {number}")
def destroy(request ,number):
    return redirect("/blogs")
def json(request):
    data={
    "title ":"My First Blog",
    "content" :"Lorem, Ipsum dolor sit amet consectetur  adipisicing elite"
    }
    return JsonResponse(data)

# Create your views here.
