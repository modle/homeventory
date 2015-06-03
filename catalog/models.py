from django.db import models

from datetime import datetime

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_location = models.CharField(max_length=50)
    item_quantity = models.IntegerField(default=1)
    entered_date = models.DateTimeField(default=datetime.now)
  
    def __str__(self):
        return self.item_name
