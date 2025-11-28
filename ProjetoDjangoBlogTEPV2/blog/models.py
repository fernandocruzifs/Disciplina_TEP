from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey("auth.User",on_delete=models.CASCADE,)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("detalhapost",kwargs={"pk": self.pk})