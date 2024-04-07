from django.shortcuts import render, get_object_or_404
from django.template import loader, Context
from django.http import HttpRequest, HttpResponse
from .models import Meldung, Kommentar
from django.views.generic import TemplateView

# Create your views here.
def meldungen(request):
    template = loader.get_template("news/meldungen.html")
    context = {'object_list': Meldung.objects.all()}
    return HttpResponse(template.render(context))

def meldung_detail(request, meldungs_id):
    template = loader.get_template('news/meldung_detail.html')
    meldung = get_object_or_404(Meldung, id=meldungs_id)
    return HttpResponse(template.render({'meldung' : meldung}))

def index(request):
    template = loader.get_template('news/home.html')
    return HttpResponse(template.render())

def login():
    template = loader.get_template('registration/login.html')
    #bitte fertig machen
def signup():
    template = loader.get_template('registration/signup.html')
    #bitte fertig machen
def password_reset_form():
    template = loader.get_template('registration/password_reset_form.html')
    #bitte fertig machen
def password_reset_done():
    template = loader.get_template('registration/password_reset_done.html')
    #bitte fertig machen
def password_reset_confirm():
    template = loader.get_template('registration/password_reset_confirm.html')
    #bitte fertig machen
def password_reset_complete():
    template = loader.get_template('registration/password_reset_complete.html')
    #bitte fertig machen