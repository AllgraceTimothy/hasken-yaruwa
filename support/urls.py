from django.urls import path
from . import views

urlpatterns = [
  path('impact/', views.impact_page, name='impact_page'),
]