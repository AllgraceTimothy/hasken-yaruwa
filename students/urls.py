from django.urls import path
from . import views

urlpatterns = [
  path('active-students/', views.active_students, name='active_students'),
  path('student-details/<int:student_id>/', views.student_details, name='student_details'),
  path('add-note', views.create_student_note, name='create_student_note'),
  path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
]