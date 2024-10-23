from tkinter.font import names
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/',views.menu, name='menu'),
    path('contact/',views.contact, name='contact'),
    path('history/',views.history, name='history'),
    path('reservations/',views.reservations, name='reservations'),
    path('send_contact/',views.send_contact, name='send_contact'),
    path('like/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('dislike/<int:comment_id>/', views.dislike_comment, name='dislike_comment'),
]
