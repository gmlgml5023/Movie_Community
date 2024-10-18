from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.

User = get_user_model()

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user)
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = PasswordChangeForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    person = User.objects.get(username=username)
    context = {
        'person': person
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    profile_owner = User.object.get(pk=user_pk)
    if request.user in profile_owner.followers.all():
        profile_owner.followers.remove(request.user)
    else:
        profile_owner.followers.add(request.user)
    return redirect('accounts:profile', profile_owner.username)