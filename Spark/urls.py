from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('aicouncil', views.council, name='council'),
    path('contact/', views.contact_view, name='contact'),
    # path('predict/', views.predict, name='predict'),
]
