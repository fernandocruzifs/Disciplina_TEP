from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey("auth.User",on_delete=models.CASCADE,)
    texto = models.TextField()
    categoria = models.ForeignKey("Categoria",on_delete=models.CASCADE,)
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("detalhapost",kwargs={"pk": self.pk})
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descricao