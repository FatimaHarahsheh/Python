from django.shortcuts import redirect, render, HttpResponse
import random
#num=random.randint(1, 100)
#Answer=False
def index(request):
    #global num
    if 'num'not in request.session:
        request.session['num']=random.randint(1, 100)
    return render(request,"index.html")
def Get_Info(requset):
    x=int(requset.session['num'])
    y= int(requset.POST['number'])
    if x==y:
        context={
            'Answer':1
            }
    elif x<y:    
        context={'Answer': 2
        }
    else :
        context={'Answer': 3
        }
    return render( requset,'index.html',context)
def delete(request):
    request.session.clear()
    request.session['num']=random.randint(1, 100)

    return redirect('/')
