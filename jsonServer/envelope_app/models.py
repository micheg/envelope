from django.db import models
from django.contrib.postgres.fields import JSONField  # Se stai usando PostgreSQL, altrimenti usa models.JSONField
from django.core.exceptions import ValidationError

class Envelope(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    data = models.JSONField(default=dict, blank=True)  # blank=True permette di lasciare il campo vuoto nel modulo

    def __str__(self):
        return self.title

    def clean(self):
        if self.data is None:
            self.data = {}
