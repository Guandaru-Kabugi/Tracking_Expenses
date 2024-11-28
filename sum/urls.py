from django.urls import path
from . import views

urlpatterns = [
    path('',views.TrackExpenses.as_view(),name='tracking'),
]