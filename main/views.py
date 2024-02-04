from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
# Create your views here.
def home(request):
    return render(request, 'main/home.html')


@login_required(login_url="/login")
def workers(request):
    return render(request, 'main/workers.html')


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        user = form.save()
        login(request, user)
        return redirect('/home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': form})
