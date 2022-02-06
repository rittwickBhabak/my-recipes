from django.urls import reverse
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    ingredients = models.TextField(blank=True, null=True)
    steps = models.TextField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("myapp:view-recipe", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title 
