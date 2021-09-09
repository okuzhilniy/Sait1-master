from django.urls import path
from . import views

urlpatterns = [
    path('', views.golowna),
    path('about-us', views.about),
    path('prikol-us', views.prikol),
    path('iz-us', views.iz),
    path('изменения-us', views.изменения),
]
