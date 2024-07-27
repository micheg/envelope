# envelope_app/management/commands/import_envelopes.py

import json
from django.core.management.base import BaseCommand
from envelope_app.models import Envelope

class Command(BaseCommand):
    help = 'Importa dati dal file JSON nel modello Envelope con un titolo fornito'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Il titolo dell\'envelope')
        parser.add_argument('json_file', type=str, help='Il percorso del file JSON')

    def handle(self, *args, **kwargs):
        title = kwargs['title']
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            # Crea o aggiorna un envelope con il titolo e i dati dal file JSON
            envelope, created = Envelope.objects.update_or_create(
                title=title,
                defaults={'data': data}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Envelope "{title}" creato con successo!'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Envelope "{title}" aggiornato con successo!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Errore durante l\'importazione: {e}'))
