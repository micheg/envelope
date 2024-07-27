# envelope_app/management/commands/cleanup_tokens.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Rimuove i token scaduti'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expiration_time = now - timedelta(hours=1)  # Imposta la durata del token (1 ora in questo caso)
        
        expired_tokens = Token.objects.filter(created__lte=expiration_time)
        count, _ = expired_tokens.delete()
        
        self.stdout.write(self.style.SUCCESS(f'{count} token scaduti rimossi.'))

