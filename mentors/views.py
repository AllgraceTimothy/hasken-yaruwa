from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mentor
from students.models import Student
from notes.models import ProgressNote
from notes.forms import ProgressNoteForm

@login_required
def mentor_dashboard(request):
  if request.user.role != 'mentor':
    messages.error(request, "Access denied.")
    return redirect('home')

  mentor = get_object_or_404(Mentor, user=request.user)

  students = Student.objects.filter(
    mentor=mentor,
    is_active=True
  ).select_related('user')

  return render(
    request,
    'mentors/mentor_dashboard.html',
    {
      'mentor': mentor,
      'students': students,
      'student_count': students.count()
    }
  )

@login_required
def mentor_student_detail(request, student_id):
  if request.user.role != 'mentor':
    messages.error(request, "Unauthorized access.")
    return redirect('home')

  mentor = get_object_or_404(Mentor, user=request.user)

  student = get_object_or_404(
    Student,
    id=student_id,
    mentor=mentor,
    is_active=True
  )

  notes = ProgressNote.objects.filter(
      student=student,
      author=student.user,
  ).select_related('author')

  return render(
    request,
    'mentors/student_detail.html',
    {'student': student, 'notes': notes}
  )

@login_required
def create_mentor_note(request, student_id):
  if request.user.role != 'mentor':
    messages.error(request, "Access denied.")
    return redirect('home')

  mentor = get_object_or_404(Mentor, user=request.user)

  student = get_object_or_404(
    Student,
    id=student_id,
    mentor=mentor,
    is_active=True
  )

  if request.method == 'POST':
    form = ProgressNoteForm(request.POST)
    if form.is_valid():
      note = form.save(commit=False)
      note.author = request.user
      note.student = student
      note.mentor = mentor
      note.save()

      messages.success(request, "Note added successfully.")
      return redirect('mentor_student_detail', student_id=student.id)
  else:
    form = ProgressNoteForm()

  return render(
    request,
    'mentors/create_note.html',
    {
      'form': form,
      'student': student
    }
  )