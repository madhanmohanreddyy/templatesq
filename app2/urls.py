from django.urls import path
from app2 import views

urlpatterns = [
    path('siva/',views.siva,name='siva')
]