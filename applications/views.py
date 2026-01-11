from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentApplicationForm,  MentorApplicationForm
from accounts.models import User, make_random_password
from students.models import Student
from mentors.models import Mentor
from accounts.utils import is_admin
from applications.models import StudentApplication, MentorApplication
from django.contrib.auth.decorators import login_required
from accounts.utils import is_admin
from django.contrib import messages
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


class SetPasswordView(PasswordResetConfirmView):
  template_name = 'applications/set_password.html'
  success_url = reverse_lazy('login')

  def form_valid(self, form):
    user = form.save()
    user.is_active = True
    user.save()
    return super().form_valid(form)

def student_application(request):
  if request.method == 'POST':
    form = StudentApplicationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('student_success_msg')
  else:
    form = StudentApplicationForm()

  return render(request, 'applications/student_application.html', {'form': form})
  
def student_success_msg(request):
  return render(request, 'applications/student_success.html')

@login_required
def review_students(request):
  if not is_admin(request.user):
    messages.error(request, 'You do not have clearance to access this page')
    return redirect('home')

  applications = StudentApplication.objects.filter(status='submitted')
  return render(
    request,
    'applications/student_applications.html',
    {'applications': applications}
  )

@login_required
def approve_student(request, application_id):
  if not is_admin(request.user):
    messages.error(request, 'You do not have clearance to access this page')
    return redirect('home')

  application = get_object_or_404(StudentApplication, id=application_id)

  if request.method == 'POST':
    action = request.POST.get('action')

    if action == 'approve':
      application.status = 'approved'
      application.save()

      # Create User properly
      password = make_random_password()
      user = User.objects.create_user(
        full_name=application.full_name,
        email=application.email,
        password=password,
        role='student',
        is_active=False,
      )

      # Create Student
      Student.objects.create(
        user=user,
        application=application,
      )

      uid = urlsafe_base64_encode(force_bytes(user.pk))
      token = default_token_generator.make_token(user)

      set_password_url = request.build_absolute_uri(
        reverse(
          'set_password',
          kwargs={'uidb64': uid, 'token':token}
        )
      )

      send_mail(
        subject='Your Student Application has been accepted',
        message=(
          f"Hello {user.full_name},\n\n"
          "Your application has been approved.\n"
          "Please click the link below to set your password and activate your account:\n\n"
          f"{set_password_url}\n\n"
          "This link can only be used once."
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
      )

      messages.success(request, "Student application approved and password setup email sent.")

    elif action == 'reject':
      application.status = 'rejected'
      application.save()

    return redirect('review_students')

  return render(
    request,
    'applications/review_student.html',
    {'application': application}
  )

def mentor_application(request):
  if request.method == 'POST':
    form = MentorApplicationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('mentor_success_msg')
  else:
    form = MentorApplicationForm()

  return render(request, 'applications/mentor_application.html', {'form': form})

def mentor_success_msg(request):
  return render(request, 'applications/mentor_success.html')

@login_required
def review_mentors(request):
  if not is_admin(request.user):
    messages.error(request, 'You do not have clearance to access this page')
    return redirect('home')

  applications = MentorApplication.objects.filter(status='submitted')
  return render(
    request,
    'applications/review_mentors.html',
    {'applications': applications}
  )

@login_required
def approve_mentor(request, application_id):
  if not is_admin(request.user):
    messages.error(request, 'You do not have clearance to access this page')
    return redirect('home')

  application = get_object_or_404(MentorApplication, id=application_id)
  
  if request.method == 'POST':
    action = request.POST.get('action')

    if action == 'approve':
      application.status = 'approved'
      application.save()

      # Create User securely
      password = make_random_password()
      user = User.objects.create_user(
        full_name=application.full_name,
        email=application.email,
        password=password,
        role='mentor',
        is_active=False,
      )

      # Create Mentor
      Mentor.objects.create(
        user=user,
        application=application,
      )

      uid = urlsafe_base64_encode(force_bytes(user.pk))
      token = default_token_generator.make_token(user)

      set_password_url = request.build_absolute_uri(
        reverse(
          'set_password',
          kwargs={'uidb64': uid, 'token':token}
        )
      )

      send_mail(
        subject='Your Mentor Application has been accepted',
        message=(
          f"Hello {user.full_name},\n\n"
          "Your application has been approved.\n"
          "Please click the link below to set your password and activate your account:\n\n"
          f"{set_password_url}\n\n"
          "This link can only be used once."
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
      )

      messages.success(request, "Mentor application approved and password setup email sent.")


    elif action == 'reject':
      application.status = 'rejected'
      application.save()

    return redirect('review_mentors')

  return render(
    request,
    'applications/review_mentor.html',
    {'application': application}
  )
