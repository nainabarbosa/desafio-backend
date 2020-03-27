from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    classificacao = models.CharField(max_length=255)


class Trip(models.Model):
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    classificacao = models.ForeignKey(Category, on_delete=models.CASCADE)
    nota = models.IntegerField(default=1, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)