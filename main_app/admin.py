from django.contrib import admin

# Register your models here.
from .models import Cat, Feeding

admin.site.register([Cat, Feeding]) # NOT admin.site.register(Cat, Feeding)bc skip the custom ModelAdmin part aka like Tries to use Feeding (a model) as a ModelAdmin class