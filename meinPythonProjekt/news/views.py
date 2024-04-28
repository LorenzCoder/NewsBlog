from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.template import loader, Context
from django.http import HttpRequest, HttpResponse
from .models import Meldung, Kommentar
from django.views.generic import TemplateView
from .forms import SignupForm

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
    template = loader.get_template('registration/signup.html')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, template, {'form': form})