from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    caffeine_content = models.CharField(max_length=100)
    image_url = models.TextField()
    price = models.CharField(max_length=10)
    extra_ingredients = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    