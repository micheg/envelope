from django.contrib import admin
from django.urls import path, include
from .views import home
from envelope_app.views import EnvelopeListView, EnvelopeDetailView, EnvelopeCreateView, EnvelopeUpdateView
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomAuthToken, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('', home, name='home'),  # URL per la pagina di cortesia
    path('api/', include([
        path('token/', CustomAuthToken.as_view(), name='api_token_auth'),
        path('envelopes/', EnvelopeListView.as_view(), name='envelope-list'),
        path('envelopes/<int:pk>/', EnvelopeDetailView.as_view(), name='envelope-detail'),
        path('envelopes/create/', EnvelopeCreateView.as_view(), name='envelope-create'),
        path('envelopes/update/<int:pk>/', EnvelopeUpdateView.as_view(), name='envelope-update'),
    ])),
]
