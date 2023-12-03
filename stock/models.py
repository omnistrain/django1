from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Groupe(models.Model):
    class Category(models.TextChoices):
        IT='IT'
        FONCTIONNEL = 'fonc'
        MANAGEMENT = 'mgt'

    name = models.fields.CharField(max_length=100)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)
    page = models.URLField(null= True, blank=True)
    creation = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    category = models.fields.CharField(choices=Category.choices, max_length=5)
    #formateur = models.fields.CharField(max_length=100) 


    def __str__(self):
        return f'{self.name}'

class Formation(models.Model):

    name = models.fields.CharField(max_length=100)
    descritpion = models.fields.CharField(max_length=1000)
    page = models.URLField(null= True, blank=True)
    groupe = models.ForeignKey(Groupe, null=True, on_delete=models.SET_NULL)
    formateur = models.fields.CharField(max_length=100) 

