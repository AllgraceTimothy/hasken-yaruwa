from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentors
from .forms import MentorForm
from django.contrib.auth.decorators import login_required
from accounts.utils import is_admin
from django.contrib import messages

def mentor_signup(request):
  if request.method == 'POST':
    form = MentorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('mentor_success')
  else:
    form = MentorForm()

  return render(request, 'mentors/signup.html', {'form': form})

def mentor_success(request):
  return render(request, 'mentors/success.html')



@login_required
def review_mentors(request):
  if not is_admin(request.user):
    return messages.error(request, 'No entry')

  mentors = Mentors.objects.filter(approved=False)
  return render(
    request,
    'mentors/review_list.html',
    {'mentors': mentors}
  )

@login_required
def approve_mentor(request, mentor_id):
  if not is_admin(request.user):
    return messages.error(request, 'No entry')

  mentor = get_object_or_404(Mentors, id=mentor_id)
  mentor.approved = True
  mentor.save()

  return redirect('review_mentors')
