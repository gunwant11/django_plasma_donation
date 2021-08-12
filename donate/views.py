from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForms, DonorForms

from .models import  DonorsInfo

def signup(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:

        form = CreateUserForms()
        if request.method == "POST":
            form = CreateUserForms(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your account was created " )

            return redirect('index')


        context = {'form': form}
        return render(request, "donate/signup.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print('login error')

        return render(request, "donate/login.html")

def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logout" )
    return redirect('index')

def index(request):
    return render(request, "donate/index.html")

@login_required(login_url='signup')
def donate(request):

    form = DonorForms()
    if request.method == "POST":
        form = DonorForms(request.POST)
        if form.is_valid():
            form.save()
            print("form sent")
            user = form.cleaned_data.get('name')
            messages.success(request, user + ", thank you for your contribution" )
            return redirect('index')
        else: 
            print('form error')
            
    context = {'form': form}
    return render(request, "donate/donate.html", context)



@login_required(login_url='signup')
def dashboard(request):
    name = request.user.username
    data = DonorsInfo.objects.all()
    if request.method == 'POST':
        message = name + ' We have successfully recived your request form Donation center 1.'

        send_mail(
            'Your Request is confirmed😊✨.',
            message,
            settings.EMAIL_HOST_USER,
            [request.user.email],
            fail_silently=False
        )
        messages.success(request, "Your request is sent" )
        return redirect('index')


    
    return render(request, "donate/dashboard.html", {'data': data })



