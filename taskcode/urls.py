from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.CodeRunApiView.as_view(), name='code_run'),
]