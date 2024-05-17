from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.template import loader, Context
from django.http import HttpRequest, HttpResponse
from .models import Meldung, Kommentar
from django.views.generic import TemplateView
from .forms import LoginForm, PasswordResetForm

# Create your views here.


def meldungen(request):
    template = loader.get_template("news/meldungen.html")
    context = {'object_list': Meldung.objects.all()}
    return HttpResponse(template.render(context))


def meldung_detail(request, meldungs_id):
    template = loader.get_template('news/meldung_detail.html')
    meldung = get_object_or_404(Meldung, id=meldungs_id)
    return HttpResponse(template.render({'meldung': meldung}))


def index(request):
    template = loader.get_template('news/home.html')
    context = {
        'request': request,
    }
    return HttpResponse(template.render(context))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})

def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request=self.request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Ungültiger Benutzername oder Password')
    return render(request, 'registration/login.html', {'form': form})

def password_reset(request):
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.succes(request, 'Eine E-mail fürs zurücksetzen des Passwortes wurde gesendet')
        return redirect('/')
    return render(request, 'registration/password_reset_done.html', {'form': form})