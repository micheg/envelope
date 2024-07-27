from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from .models import Envelope

@admin.register(Envelope)
class EnvelopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'data')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

