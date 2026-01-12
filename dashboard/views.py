from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages

from accounts.utils import is_admin
from applications.models import StudentApplication, MentorApplication
from mentors.models import Mentor
from students.models import Student
from support.models import Support

@login_required
def admin_dashboard(request):
  if not is_admin(request.user):
    messages.error(request, 'ou are not allowed to access this page')

  context = {
    'pending_applications': StudentApplication.objects.filter(status='submitted').count(),
    'approved_students': Student.objects.filter(user__is_active=True).count(),
    'pending_mentors': MentorApplication.objects.filter(status='submitted').count(),
    'total_support': Support.objects.aggregate(
        total=Sum('amount')
    )['total'] or 0,
  }

  return render(request, 'dashboard/admin_dashboard.html', context)