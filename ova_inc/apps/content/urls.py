from . import views
from django.urls import path

app_name = 'content'
urlpatterns = [
    path('test/', views.tests, name="test")
]
