from django.urls import path
from . import views
from .views import SetPasswordView

#app_name = 'applications'

urlpatterns = [
  path('student_application/', views.student_application, name='student_application'),
  path('student_success/', views.student_success_msg, name='student_success_msg'),
  path('review_students/', views.review_students, name='review_students'),
  path('approve_student/<int:application_id>/', views.approve_student, name='approve_student'),
  path('mentor_application/', views.mentor_application, name='mentor_application'),
  path('mentor_success/', views.mentor_success_msg, name='mentor_success_msg'),
  path('review_mentors/', views.review_mentors, name='review_mentors'),
  path('approve_mentor/<int:application_id>/', views.approve_mentor, name='approve_mentor'),
  path('set-password/<uidb64>/<token>/', SetPasswordView.as_view(), name='set_password'),
]