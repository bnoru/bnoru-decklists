from django.contrib import admin
from .models import Decklist
from tinymce.widgets import TinyMCE
from django.db import models

class DecklistAdmin(admin.ModelAdmin):
    
    fields = ["decklist_title",
              "decklist_maindeck",
              "decklist_sideboard",
              "decklist_published"]
    

admin.site.register(Decklist, DecklistAdmin)