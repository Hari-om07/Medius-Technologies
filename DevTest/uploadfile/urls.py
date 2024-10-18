# upload/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),  # This will map to your file upload view
]
