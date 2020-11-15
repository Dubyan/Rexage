from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserCreationForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from .models import Tour
from .forms import TourForm





def index(request):
    return render(request, 'main/index.html')


def sport(request):
    return render(request, 'main/sport.html')


def climat(request):
    return render(request, 'main/climat.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):

        form.save()

        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
        form_class = AuthenticationForm

        template_name = "login.html"

        success_url = "/"

        def form_valid(self, form):
            self.user = form.get_user()

            login(self.request, self.user)
            return super(LoginFormView, self).form_valid(form)


def water(request):
    return render(request, 'main/water.html')


def ural(request):
    return render(request, 'main/ural.html')


def sakmara(request):
    return render(request, 'main/sakmara.html')


def geogr(request):
    return render(request, 'main/geogr.html')


def maps(request):
    return render(request, 'main/maps.html')


def list(request):
    tours = Tour.objects.all()
    return render(request, 'main/list.html', {'title': 'Пользовательские маршруты', 'tours': tours})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
        else:
            error = 'Error'

    form = TourForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def pal(request):
    return render(request, 'main/pal.html')


def gl(request):
    return render(request, 'main/gl.html')


def kuv(request):
    return render(request, 'main/kuv.html')

