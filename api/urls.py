from django.urls import path

from api.views import HomeView

urlpatterns = [
    path('api', HomeView.as_view(), name='api'),
]
