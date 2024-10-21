from django.shortcuts import render

def home(request):
    return render(request, 'Menu/home.html')  # Chemin vers home.html dans le dossier Menu
def menu(request):
    plats = Menu.objects.all()
    return render(request, 'Menu/menu.html', {'plats': plats})
def contact(request):
    return render(request, 'Menu/contact.html')
def history(request):
    return render(request, 'Menu/history.html')
def reservations(request):
    return render(request, 'Menu/reservations.html')
def send_contact(request):
    return render(request, 'Menu/send_contact')
