from django.urls import path
from . import views

urlpatterns = [
    path('', views.historia_view, name='inicio'),
    path('mecanicas/', views.pagina_view, name='mecanicas'),
    path('visual/', views.visual_view, name='visual'),
    path('contacto/', views.contacto_view, name='contacto'),
]
