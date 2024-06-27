from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.template import loader, Context
from django.http import HttpRequest, HttpResponse
from .models import Meldung, Kommentar
from django.views.generic import TemplateView
from .forms import LoginForm, LoginForm

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