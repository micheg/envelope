from django.db import models
from django.contrib.postgres.fields import JSONField  # Se stai usando PostgreSQL, altrimenti usa models.JSONField

class Envelope(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    data = models.JSONField(default=dict)  # Usa dict per un oggetto JSON vuoto come valore predefinito

    def __str__(self):
        return self.title

