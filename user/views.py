from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Here you would normally log the user in by setting a session
                messages.success(request, 'Login successful.')
                return redirect('home')  # Redirect to a home page or dashboard
            else:
                messages.error(request, 'Invalid credentials.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')