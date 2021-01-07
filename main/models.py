from django.db import models
from datetime import datetime

# Create your models here.
class Decklist(models.Model):
    decklist_title = models.CharField(max_length=200)
    decklist_format = models.CharField(max_length=200)
    decklist_maindeck = models.TextField()
    decklist_sideboard = models.TextField()
    decklist_published = models.DateTimeField("date published", default=datetime.now)
    
    def __str__(self):
        return self.decklist_title
    
    