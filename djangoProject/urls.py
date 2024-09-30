from django.contrib import admin
from django.urls import path
from . import views  # Importer tes vues (si tu utilises les vues directement dans ce fichier)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route pour afficher home.html
]
