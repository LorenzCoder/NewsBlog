from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    #path('password_reset_form/', views.password_reset_form, name='Password Reset'),
    path('meldungen/', views.meldungen, name='meldungen'),
    path('meldungen/<int:meldungs_id>/', views.meldung_detail, name='meldung_detail'),
]