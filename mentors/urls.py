from django.urls import path
from . import views

urlpatterns = [
  path('mentor-dashboard', views.mentor_dashboard, name='mentor_dashboard'),
  path('mentor-student-details/<int:student_id>/', views.mentor_student_detail, name='mentor_student_detail'),
  path('student/<int:student_id>/add-note/', views.create_mentor_note, name='create_mentor_note'),
]