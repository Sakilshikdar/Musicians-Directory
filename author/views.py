from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# Create your views here.
from django.urls import reverse_lazy


def register(request):
    if request.method == "POST":
        signup_form = forms.RegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('user_login')
    else:
        signup_form = forms.RegistrationForm()
    return render(request, 'register.html', {'data': signup_form, 'type': 'Register'})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                messages.success(request, 'login successfully')
                login(request, user)
                return redirect('user_login')
            else:
                messages.warning(request, 'login information are incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'data': form, 'type': 'login'})


class LoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('musician')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged information is incorrect')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def user_logout(request):
    logout(request)
    return redirect('musician')
