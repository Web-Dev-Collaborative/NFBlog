from django.urls import path

from . import views

urlpatterns = [
    path('', views.people, name="people"),
    path('add_person/', views.add_person, name="add_person"),
    path('update_person/<slug:person_slug>', views.update_person, name="update_person"),
    path('<slug:person_slug>', views.person, name="person"),
]
