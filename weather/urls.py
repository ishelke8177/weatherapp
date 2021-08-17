from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('about/',views.about,name='about'),
]
