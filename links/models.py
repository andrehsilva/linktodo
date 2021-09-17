from django.db import models
from datetime import date
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.models import User

# Create your models here.

class CategoriaLinks(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Categoria de Link'

    def __str__(self):
        return self.nome



class Links(models.Model):
    escola = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    tenant_id = models.CharField(max_length=100)
    school_id = models.CharField(max_length=100)
    acessar = models.CharField(max_length=50)
    login = models.CharField(max_length=50, blank=True)
    senha = models.CharField(max_length=70, blank=True)
    data_cadastro = models.DateField(default=date.today)
    categoria = models.ForeignKey(CategoriaLinks, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=DO_NOTHING)

    class Meta:
        verbose_name = 'Link'

    def __str__(self):
        return self.escola