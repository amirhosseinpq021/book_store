from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SingUpView.as_view(), name='signup'),

]
