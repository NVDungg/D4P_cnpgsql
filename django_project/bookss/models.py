import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    author_review = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    about = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="cover/", blank=True)

    class Meta:
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])      # other way call id. make it to string return in http
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews",)
    review = models.CharField(max_length=500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("book_list")
    
    def __str__(self):
        return self.review
    