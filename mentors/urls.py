from django.urls import path
from . import views

urlpatterns = [
  path('signup/', views.mentor_signup, name='mentor_signup'),
  path('mentor_success/', views.mentor_success, name='mentor_success'),
  path('review/', views.review_mentors, name='review_mentors'),
  path('approve/<int:mentor_id>/', views.approve_mentor, name='approve_mentor'),
]