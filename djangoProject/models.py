from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    chef = models.ForeignKey('Chef', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(default=0.00)

    def __str__(self):
        return self.name
