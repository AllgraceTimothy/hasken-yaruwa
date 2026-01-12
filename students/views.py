from django.shortcuts import render, redirect, get_object_or_404
from accounts.utils import is_admin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student
from mentors.models import Mentor
from notes.models import ProgressNote
from notes.forms import ProgressNoteForm

@login_required
def active_students(request):
  if not is_admin(request.user):
    messages.error(request, "Access denied.")
    return redirect('home')

  students = Student.objects.filter(
    application__status='approved',
    user__is_active=True,
  ).select_related('user', 'mentor')

  return render(
    request,
    'students/active_students.html',
    {'students': students}
  )

@login_required
def student_details(request, student_id):
  if not is_admin(request.user):
    messages.error(request, "Access denied.")
    return redirect('home')

  student = get_object_or_404(
    Student.objects.select_related('user', 'mentor'),
    id=student_id,
    user__is_active=True
  )

  mentors = Mentor.objects.filter(
    user__is_active=True
  ).select_related('user')

  if request.method == 'POST':
    mentor_id = request.POST.get('mentor')
    mentor = get_object_or_404(Mentor, id=mentor_id)

    student.mentor = mentor
    student.save()

    messages.success(request, "Mentor assigned successfully.")
    return redirect('active_students')
  
  return render(
    request,
    'students/student_details.html',
    {
      'student': student,
      'mentors': mentors
    }
  )

@login_required
def student_dashboard(request):
  if request.user.role != 'student':
    messages.error(request, "Access denied.")
    return redirect('home')

  student = get_object_or_404(
    Student,
    user=request.user,
    user__is_active=True
  )

  mentor = student.mentor

  notes = ProgressNote.objects.filter(
    student=student,
    author=mentor.user,
    is_visible_to_student=True
  ).select_related('author')[:10]

  return render(
    request,
    'students/student_dashboard.html',
    {
      'student': student,
      'mentor': mentor,
      'notes': notes
    }
  )

@login_required
def create_student_note(request):
  if request.user.role != 'student':
    messages.error(request, "Access denied.")
    return redirect('home')

  student = get_object_or_404(Student, user=request.user, user__is_active=True)

  mentor = student.mentor
  if not mentor:
    messages.error(request, "No mentor assigned yet.")
    return redirect('student_dashboard')

  if request.method == 'POST':
    form = ProgressNoteForm(request.POST)
    if form.is_valid():
      note = form.save(commit=False)
      note.author = request.user
      note.student = student
      note.mentor = mentor
      note.is_visible_to_student = True
      note.save()

      messages.success(request, "Update submitted successfully.")
      return redirect('student_dashboard')
  else:
      form = ProgressNoteForm()

  # hide visibility field for students
  form.fields.pop('is_visible_to_student')

  return render(
    request,
    'students/create_note.html',
    {'form': form}
  )
