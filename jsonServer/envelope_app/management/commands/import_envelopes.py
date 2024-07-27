# envelope_app/management/commands/import_envelopes.py

import json
from django.core.management.base import BaseCommand
from envelope_app.models import Envelope

class Command(BaseCommand):
    help = 'Importa dati dal file JSON nel modello Envelope'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Il percorso del file JSON')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            for item in data:
                Envelope.objects.update_or_create(
                    id=item.get('id'),
                    defaults={
                        'title': item.get('title'),
                        'data': item.get('data')
                    }
                )

            self.stdout.write(self.style.SUCCESS('Importazione completata con successo!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Errore durante l\'importazione: {e}'))
