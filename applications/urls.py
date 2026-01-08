from django.urls import path
from . import views

urlpatterns = [
  path('apply/', views.apply_for_support, name='apply'),
  path('success/', views.successful_application, name='successful_application'),
  path('review/', views.review_applications, name='review_applications'),
  path('review/<int:application_id>/', views.review_application_detail, name='review_application_detail'),
]