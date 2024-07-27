from rest_framework import generics
from .models import Envelope
from .serializers import EnvelopeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Lista tutti gli envelope (id e title)
class EnvelopeListView(generics.ListAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        envelopes = self.get_queryset().values('id', 'title')
        return Response(envelopes)

# Ritorna il campo JSON dato l'id
class EnvelopeDetailView(generics.RetrieveAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        envelope_id = kwargs.get('pk')
        envelope = self.get_queryset().filter(id=envelope_id).values('data').first()
        if envelope:
            return Response(envelope['data'])
        return Response(status=status.HTTP_404_NOT_FOUND)

# Crea un nuovo envelope
class EnvelopeCreateView(generics.CreateAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        data = request.data.get('data')
        envelope = Envelope.objects.create(title=title, data=data)
        return Response({
            'id': envelope.id,
            'title': envelope.title,
            'data': envelope.data
        }, status=status.HTTP_201_CREATED)
