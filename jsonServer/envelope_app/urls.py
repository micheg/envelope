from django.urls import path
from .views import EnvelopeListView, EnvelopeDetailView, EnvelopeCreateView

urlpatterns = [
    path('envelopes/', EnvelopeListView.as_view(), name='envelope-list'),
    path('envelopes/<int:pk>/', EnvelopeDetailView.as_view(), name='envelope-detail'),
    path('envelopes/create/', EnvelopeCreateView.as_view(), name='envelope-create'),
]

