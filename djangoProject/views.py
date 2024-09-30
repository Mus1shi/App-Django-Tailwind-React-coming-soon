from django.shortcuts import render

def home(request):
    return render(request, 'Menu/home.html')  # Chemin vers home.html dans le dossier Menu
