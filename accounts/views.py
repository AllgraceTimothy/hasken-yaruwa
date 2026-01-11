from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(
      request,
      email=email,
      password=password
    )

    if user is not None:
      login(request, user)

      # Redirect based on role
      if user.role == 'admin':
        return redirect('admin_dashboard')
      elif user.role == 'mentor':
        return redirect('mentor_dashboard')
      elif user.role == 'student':
        return redirect('student_dashboard')
      else:
        return redirect('home')
    else:
      messages.error(
        request,
        'Invalid email or password.'
      )

  return render(request, 'accounts/login.html')

def logout_view(request):
  logout(request)
  return redirect('login')
