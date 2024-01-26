# accounts/views.py
from django.contrib.auth import logout
# from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm  # Replace with your actual form







class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Account created successfully!')
        return response




# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"



def custom_logout(request):
    logout(request)
    # Redirect to your home page or any other desired URL after logout
    return redirect('home')





























