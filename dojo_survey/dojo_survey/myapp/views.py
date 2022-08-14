import re
from typing import ContextManager
from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,"index.html")
def result(request):
    fname=request.POST["fname"]
    location=request.POST["location"]
    Language=request.POST["Language"]
    comment=request.POST["comment"]
    context={
        "fname":fname,
        "location":location,
        "Language":Language,
        "comment":comment

    }
    return render(request,"result.html",context)

