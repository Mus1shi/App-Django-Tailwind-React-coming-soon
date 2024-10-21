from django.contrib import admin
from .models import Menu, Category, Chef  # Importe tes modèles

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Chef)
