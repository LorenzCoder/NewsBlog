from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('meldungen/', views.meldungen, name='meldungen'),
    path('meldungen/<int:meldungs_id>/', views.meldung_detail, name='meldung_detail'),
]