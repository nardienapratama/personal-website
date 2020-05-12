from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Schedule, Registration
from .forms import Activity_Form, Registration_Form
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json

# Create your views here.

def index(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'aboutme.html')

def books(request):
    # num_fav = request.POST['counter']
    user = request.user
    # user = authenticate(request, num_fav = num_fav)

    if user is not None:
        user_session = request.session.get('user_session', 'private')
        request.session['user_session'] = 'private'

        return render(request, 'books.html')

    else:
        del request.session['user_session']      
        return render(request, 'books.html')

def signup(request):
    return render(request, 'signup.html')



def schedule(request):
    if request.method=="POST":
        form = Activity_Form(request.POST)
        if form.is_valid():
                cleaned_data = form.cleaned_data
                schedule = Schedule.create(eventName=cleaned_data['eventName'],
                            date=cleaned_data['date'], time=cleaned_data['time'],
                            category=cleaned_data['category'], location=cleaned_data['location'])
                schedule.save()
                return HttpResponseRedirect('/schedule')
        else:
                return HttpResponseRedirect('/schedule')
    else:
        form = Activity_Form()
        return render(request, 'schedule.html', {'form':form, "schedules":Schedule.objects.all()})


def delete_events(request):
    Schedule.objects.all().delete()
    return HttpResponseRedirect('/schedule')


def display_regis_form(request):
    response = {}
    form = Registration_Form(request.POST or None)
    response['form'] = form
    return render(request, 'registration.html', response)

def run_form(request):
    if request.method == 'POST':    
        form = Registration_Form(request.POST)
        if form.is_valid():
                cleaned_data = form.cleaned_data
                registrationinput = Registration.create(firstname=cleaned_data['firstname'], lastname=cleaned_data['lastname'], username=cleaned_data['username'], email=cleaned_data['email'], password=cleaned_data['password'])
                registrationinput.save()
                # #Create user and save to database
                # user = User.objects.create_user(cleaned_data['username'], cleaned_data['email'])

                # #Update fields and then save again
                # user.first_name = cleaned_data['firstname']
                # user.last_name = cleaned_data['lastname']
                # user.save()
                return JsonResponse(registrationinput)

                        
        else:
                registrationinput = {}
                return JsonResponse(registrationinput)

@csrf_exempt
def email_validation(request):
    currentemail = request.POST.get('email', None)
    validation = {
            'isExist' : Registration.objects.filter(email=currentemail).exists()
    }
    return JsonResponse(validation)

def registerPage(request):
    response = {}
    return render(request, 'register.html'. response)

def loginPage(request):
    
