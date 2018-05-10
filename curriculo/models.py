from django.db import models

# Create your models here.
class Curso(models.Model):
    #id = models.IntegerField(unique=True)
    nome = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'Curso'