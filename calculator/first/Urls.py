from django.urls import path
from . import views

urlpatterns=[
    path('',views.base,name='base'),
    path('selection/',views.vselection,name='vsc'),
    path('output/', views.output, name='output'),
]