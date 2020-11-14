from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserCreationForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView





def index(request):
    return render(request, 'main/index.html')


def sport(request):
    return render(request, 'main/sport.html')


def climat(request):
    return render(request, 'main/climat.html')


def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'sussss' )
        else:
            if form.is_valid():

              ins = form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        user = authenticate(username=username, password=password)
        return redirect('/')


    else:
        form = UserCreationForm()

        context = {'form': form}
        return render(request, 'register.html', context)


def water(request):
    return render(request, 'main/water.html')


def ural(request):
    return render(request, 'main/ural.html')


def sakmara(request):
    return render(request, 'main/sakmara.html')


def geogr(request):
    return render(request, 'main/geogr.html')

