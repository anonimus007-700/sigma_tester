from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import RegForm, LoginForm

def main(request):
    if request.user.is_authenticated:
        return render(request, 'client/main.html',
                      {'users': User.objects.get(username=request.user)})
    else:
        return render(request, 'client/main.html')

def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)

        try:
            user = User.objects.create_user(form['username'].value(),
                                            form['email'].value(),
                                            form['password'].value())
            user.save()
            auth_login(request, user)

            return redirect('/client/')
        except:
            return render(request, 'client/register.html', {'form': RegForm(),
                                                            'error': True})

    if not request.user.is_authenticated:
        return render(request, 'client/register.html', {'form': RegForm()})
    else:
        return redirect('/client/')

def login(request):
    if request.method == "POST":
        user = User.objects.all()
        form = LoginForm(request.POST)

        user = authenticate(username=form['username'].value(),
                            password=form['password'].value())

        if user is not None:
            auth_login(request, user)
            return redirect('/client/')

    if not request.user.is_authenticated:
        return render(request, 'client/login.html', {'form': LoginForm()})
    else:
        return redirect('/client/')

def logout(request):
    auth_logout(request)
    return redirect('/client/')
