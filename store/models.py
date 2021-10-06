from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    
    def __str__(self):
        return f"{self.id} {self.title} by {self.author}"
    