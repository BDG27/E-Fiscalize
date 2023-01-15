from django.urls import path
from .. import views

urlpatterns = [
    path('', views.Company.index, name='company_index'),
] 
