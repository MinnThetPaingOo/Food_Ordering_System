from django.db import models

# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=20)
    description = models.TextField()
    availability = models.BooleanField()
    def __str__(self):
        return self.menu_name

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,related_name="items")
    description = models.TextField()
    calories = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.item_name