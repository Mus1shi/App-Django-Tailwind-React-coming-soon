from django.shortcuts import render, get_object_or_404
from djangoProject.models import Category, Menu  # Importer les modèles Category et Menu

def home(request):
    return render(request, 'Menu/home.html')  # Chemin vers home.html dans le dossier Menu

def menu(request):
    # Récupérer les catégories
    premiere_selection = get_object_or_404(Category, name='Première Sélection')
    deuxieme_selection = get_object_or_404(Category, name='Deuxième Sélection')
    troisieme_selection = get_object_or_404(Category, name='Troisième Sélection')

    # Récupérer les plats par catégorie
    plats_premiere_selection = Menu.objects.filter(category=premiere_selection)
    plats_deuxieme_selection = Menu.objects.filter(category=deuxieme_selection)
    plats_troisieme_selection = Menu.objects.filter(category=troisieme_selection)

    # Passer les plats et les prix des sous-catégories au template
    context = {
        'plats_premiere_selection': plats_premiere_selection,
        'plats_deuxieme_selection': plats_deuxieme_selection,
        'plats_troisieme_selection': plats_troisieme_selection,
    }

    return render(request, 'Menu/menu.html', context)

def contact(request):
    return render(request, 'Menu/contact.html')

def history(request):
    return render(request, 'Menu/history.html')

def reservations(request):
    return render(request, 'Menu/reservations.html')

def send_contact(request):
    return render(request, 'Menu/send_contact')
