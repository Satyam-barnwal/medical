from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from .models import Doctor
from .forms import SignupForm, AppointmentForm, ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import AppointmentDetails
from django.template import loader
# Create your views here.


def home(request):
#     doctors = Doctor.objects.all()r
     return render(request,'home.html') #{'doctors':doctors})


def about(request):
    return render(request, 'about.html')


    # if request.method == 'POST':
    #     form = AppointmentForm(request.POST)
    #     if form.is_valid():
    #         messages.success(request, 'successfullly submited')
    #         form.save()
    # else:
    #     form = AppointmentForm()
    # return render(request, 'contact.html', {'form': form})


def appointment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                messages.success(request, 'successfullly submited')
                form.save()
        else:
            form = AppointmentForm()
        return render(request, 'appointment.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'successfullly submited')
            form.save()
    else:
        form = SignupForm()
    return render(request, 'signup.html',{'form':form})

def rawlogin(request):
    return render(request,'login.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'userlogin.html', context={'form': AuthenticationForm()})

def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in')
                return HttpResponseRedirect('/doctor_schedule/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'doctorlogin.html', context={'form': AuthenticationForm()})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'successfully submitted')
            form.save()

    else:
        form = ContactForm()
    return render(request, 'contact.html',{'form':form})

def schedule(request):
    doctor_name = request.user.get_full_name()
    appointmentdata = AppointmentDetails.objects.filter(consultant=request.user.get_full_name()).values()
    template = loader.get_template('doctor_schedule.html')
    context = {
        'name': doctor_name,
        'appointmentdata': appointmentdata,
    }
    print(appointmentdata)
    return HttpResponse(template.render(context, request))