from django.urls import path

from . import views

urlpatterns = [
    path("<str:story_id>/", views.index, name="index"),
    path("character/<str:character>/", views.results, name="results"),
]