from django.urls import path
from . import views

urlpatterns = [
    path('total/',views.TrackExpenses.as_view(),name='tracking'),
]