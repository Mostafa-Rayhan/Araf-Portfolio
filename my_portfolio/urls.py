
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/form_submission', views.form_submission, name='form_submission'),

]
