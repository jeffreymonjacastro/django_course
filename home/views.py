from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm



# def home(request):
#   return HttpResponse("Hello, world!")

## Template
# def home(request):
#   return render(request, 'home/welcome.html', {
#     'today': datetime.today()
#   })

## Class-based view
class HomeView(TemplateView):
  template_name = 'home/welcome.html'
  extra_content = {'today': datetime.today()}


## Access template by login 
# @login_required(login_url='/admin')
# def authorized(request):
#   return render(request, 'home/authorized.html', {})

## Class-based view
class AuthorizedView(LoginRequiredMixin, TemplateView):
  template_name = 'home/authorized.html'
  login_url = '/admin'


class LoginInterfaceView(LoginView):
  template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
  template_name = 'home/logout.html'


class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'home/signup.html'
  success_url = '/login'

  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('notes.list')
    return super().get(request, *args, **kwargs)