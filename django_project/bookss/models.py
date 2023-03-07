import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])      # other way call id. make it to string return in http
    
    def __str__(self):
        return self.title