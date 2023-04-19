from django.shortcuts import render,redirect
import datetime
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold']= 0
    if 'activities' not in request.session:
        request.session['activities']=[]
    return render(request,'index.html')

def pros(request):
    if request.method == "POST":
        if request.POST['action'] == "farm":
            money = random.randrange(10, 20)
            request.session['gold'] += money
            request.session['activities'].append(
                'Earned ' + str(money) + ' gold from the farm! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 14:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['action'] == "cave":
            money = random.randrange(5, 10)
            request.session['gold'] += money
            request.session['activities'].append(
                'Earned ' + str(money) + ' gold from the cave! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 14:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['action'] == "house":
            money = random.randrange(2, 5)
            request.session['gold'] += money
            request.session['activities'].append(
                'Earned ' + str(money) + ' gold from the house! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 14:
                request.session['activities'].pop(0)
            len(request.session['activities'])
            return redirect('/')
        elif request.POST['action'] == "casino":
            money = random.randrange(-50, 50)
            request.session['gold'] += money
            if money < 0:
                request.session['activities'].append(
                    'Entered a casino and Won ' + str(money) + ' gold! Ouch! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
                if len(request.session['activities']) >= 14:
                    request.session['activities'].pop(0)
                return redirect('/')
            else:
                request.session['activities'].append(
                    'Entered a casino and Lost ' + str(money)+ ' '+
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
                if len(request.session['activities']) >= 14:
                    request.session['activities'].pop(0)
                return redirect('/')
    else:
        return redirect('/')
def clear(request):
    request.session.clear()
    return redirect('/')