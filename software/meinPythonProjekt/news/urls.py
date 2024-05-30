from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('meldungen/', views.meldungen, name='meldungen'),
    path('meldungen/<int:meldungs_id>/', views.meldung_detail, name='meldung_detail'),
]
