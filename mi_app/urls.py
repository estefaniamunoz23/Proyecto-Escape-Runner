from django.urls import path
from . import views

urlpatterns = [
    path('', views.historia_view, name='historia'),
    path('visual/', views.visual_view, name='visual'),
]