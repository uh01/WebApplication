from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import BoughtCar


def home(request):
    return render(request, 'home.html')



def user_signin(request):
    if request.method == 'POST':
        signin_form = forms.RegistrationForm(request.POST)
        if signin_form.is_valid():
            signin_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('home')
    
    else:
        signin_form = forms.RegistrationForm()
    return render(request, 'user_signin.html', {'form' : signin_form, 'type' : 'Sign-in'})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('user_signin')
    else:
        form = AuthenticationForm()
        return render(request, 'user_login.html', {'form' : form, 'type' : 'Log-in'})



class UserLoginView(LoginView):
    template_name = 'user_signin.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context



@login_required
def user_profile(request):
    bought_cars = BoughtCar.objects.filter(user=request.user)

    return render(request, 'user_profile.html', {'bought_cars': bought_cars, 'type': 'Profile'})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('user_profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'edit_profile.html', {'form' : profile_form, 'type' : 'Profile-Update'})
    


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('user_profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form, 'type' : 'Password-Update'})



def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully')
    return redirect('home')