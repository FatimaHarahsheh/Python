from django.shortcuts import render, HttpResponse,redirect
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=1
    else:
        request.session['counter']+=1

    return render(request,'index.html')
def delete(request):
    request.session['counter']=0
    return redirect('/')