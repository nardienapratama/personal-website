from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Schedule, Registration
from .forms import Activity_Form, Registration_Form, CreateUserForm
import json

# Create your views here.

def index(request):
    return redirect('login')

def home(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'aboutme.html')

def books(request):
    # num_fav = request.POST['counter']
    user = request.user
    # user = authenticate(request, num_fav = num_fav)
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = authenticate(request, username=username, password=password)

    # if user.is_anonymous:      
        # del request.session['user_session'] 
        # return render(request, 'books.html')
    # if request.user.is_authenticated():
       

    # else:
        # if request.session.get('username'):
        # request.session['username']
        # print(request.session['username'])
        # return render(request, 'books.html')

        # if 'username' in request.session:   
        #     print("this works")
        #     username = request.session.get('username','private')
        #     request.session['username'] = 'private'
        #     print("this works 2")
        #     return render(request, 'books.html')
    if user.is_anonymous:
        # del request.session['username']      
        return render(request, 'books.html')
            
    else:
        # num_visits = request.session.get('num_visits', 0)
        # request.session['num_visits'] = num_visits + 1

        user_session = request.session.get('username', 'private')
        request.session['username'] = 'private'

        # num_fav = request.POST['counter']
        # request.session['user_session']['favbooks'] = num_fav
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
                registrationinput = Registration.create(firstname=cleaned_data['firstname'], lastname=cleaned_data['lastname'], email=cleaned_data['email'], password=cleaned_data['password'])
                registrationinput.save()

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
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    response = {'form': form}
    return render(request, 'register.html', response)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user is authenticated
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            if 'next' in request.POST:
                # return HttpResponseRedirect(request.POST.get['next'])
                return redirect('home')
            else:
                return redirect('home')
            
            # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

        else:
            messages.info(request, 'Username OR password is incorrect')
    
    response = {}
    return render(request, 'login.html', response)

def logoutUser(request):
    if 'action' in request.GET:
        action = request.GET.get('action')
        if action == 'logout':
            if request.session.has_key('username'):
                request.session.flush()
    # del request.session['username'] 
    logout(request)
    return redirect('login')
