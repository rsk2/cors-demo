from cors_app.views import HomeView
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]