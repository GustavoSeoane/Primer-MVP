from django.urls import path
from changos.views import changos

urlpatterns = [
    path('', changos, name = 'changos'),        
]
