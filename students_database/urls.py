from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('guardian-list/', views.gurdian_list, name='guardian-list'),
    path('guardian-details/<g_id>/', views.guardian_details, name='guardian-details'),
    path('list/', views.students_list, name='students-list'),
    # path('school-details/<school_id>/', views.school_details, name='school-details'),
]