from tkinter.font import names

from django.contrib import admin
from django.urls import path
from . import views  # Importer tes vues (si tu utilises les vues directement dans ce fichier)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/',views.menu, name='menu'),
    path('contact/',views.contact, name='contact'),
    path('history/',views.history, name='history'),
    path('reservations/',views.reservations, name='reservations'),
    path('send_contact/',views.send_contact, name='send_contact')


]
