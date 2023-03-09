from django.urls import path
from .views import CopyCreatelView, CopyDateilView


urlpatterns = [
    path("copies/", CopyCreatelView.as_view()),
    path("copies/<int:copy_id>/", CopyDateilView.as_view()),
]
