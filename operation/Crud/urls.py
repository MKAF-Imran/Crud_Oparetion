
from django.urls import path
from . import views
urlpatterns = [


    path('', views.index ,name ='index'),
    path('create/', views.create ,name ='create'),
    path('add_employee/', views.add_employee ,name ='add_employee'),
    path('edit/<id>/', views.edit ,name ='edit'),
    path('delete/<id>/', views.delete ,name ='delete'),
    path('update/<id>/', views.update  ,name ='delete'),

]
