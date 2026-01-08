from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from students.models import Student
from accounts.utils import is_admin
from applications.models import Application
from django.contrib.auth.decorators import login_required
from accounts.utils import is_admin
from django.contrib import messages


def apply_for_support(request):
  if request.method == 'POST':
    form = ApplicationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('successful_application') # Will create an application successful message later
  else:
    form = ApplicationForm()

  return render(request, 'applications/apply.html', {'form': form})
  
def successful_application(request):
  return render(request, 'applications/success.html')

@login_required
def review_applications(request):
  if not is_admin(request.user):
    messages.error(request, 'You do not have clearance to acces this page')

  applications = Application.objects.filter(status='submitted')
  return render(
    request,
    'applications/review_list.html',
    {'applications': applications}
  )
  
@login_required
def review_application_detail(request, application_id):
  if not is_admin(request.user):
    messages.error(request, 'You do not have clearance to acces this page')

  application = get_object_or_404(Application, id=application_id)

  if request.method == 'POST':
    action = request.POST.get('action')

    if action == 'approve':
      application.status = 'approved'
      application.save()
      Student.objects.create(application=application)

    elif action == 'reject':
      application.status = 'rejected'
      application.save()

    return redirect('review_applications')

  return render(
    request,
    'applications/review_details.html',
    {'application': application}
  )
