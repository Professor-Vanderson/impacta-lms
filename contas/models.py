import uuid
from django.db import models

# Create your models here.
class Usuario(models.Model):

    email = models.EmailField(max_length=130,unique=True)
    senha = models.CharField(max_length=140)

    def __str__(self):
        return self.email

class Sessao(models.Model):

        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)