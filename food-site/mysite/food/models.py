from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=500, default='https://w7.pngwing.com/pngs/1013/530/png-transparent-cafe-italian-cuisine-breakfast-menu-eat-food-logo-eating-thumbnail.png')

    def __str__(self):
        return self.name
    
