from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.school_list, name='school-list'),
    path('school-details/<school_id>/', views.school_details, name='school-details'),
]