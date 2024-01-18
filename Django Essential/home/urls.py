from django.urls import path
from . import views

urlpatterns = [
  path('', views.HomeView.as_view()), ## Class-based view
  path('authorized/', views.AuthorizedView.as_view()),
  path('login/', views.LoginInterfaceView.as_view(), name='login'),
  path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
  path('signup/', views.SignUpView.as_view(), name='signup'),
]