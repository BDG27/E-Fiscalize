from django.urls import path
from .. import views

urlpatterns = [
    path('company/', views.Company.index, name='company_index'),
] 
