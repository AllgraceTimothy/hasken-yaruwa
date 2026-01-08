from django.shortcuts import render, redirect
from students.models import Student
from support.models import Support
from django.db.models import Sum

def home(request):
  total_students = Student.objects.filter(is_active=True).count()
  total_support = Support.objects.aggregate(
    total=Sum('amount')
  )['total'] or 0

  context = {
    'total_students': total_students,
    'total_support': total_support,
  }

  return render(request, 'pages/home.html', context)

def about(request):
  return render(request, 'pages/about.html')

def support_page(request):
  total_support = Support.objects.aggregate(
    total=Sum('amount')
  )['total'] or 0

  return render(
    request,
    'pages/support.html',
    {'total_support': total_support}
  )