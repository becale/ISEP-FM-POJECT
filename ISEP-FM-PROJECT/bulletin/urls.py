from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('bulletin/', views.bulletin, name="bulletin"),
    path('notes/', views.notes, name="notes"),
    path('kds/', views.EtudiantApi, name="etudiantAPI"),
    path('UeAPI/', views.UEAPI, name='UeAPI)'),
    path('etudiantStaps1/', views.EtudiantNiveau1Staps, name="etudiantstaps1")
]

