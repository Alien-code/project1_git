from django.shortcuts import render
from .models import Guardian
from .models import Students

# Create your views here.
def gurdian_list(request):
    all_gurdian = Guardian.objects.all()
    return render(request, 'student/guardian-list.html', {'gurdian_list': all_gurdian})

# creating a function for showing single guardian details when click on guardian name from student table


def guardian_details(request, g_id):
    single_guardian = Guardian.objects.get(pk=g_id)
    return render(request, 'student/guardian-details.html', {'guardian': single_guardian})


def students_list(request):
    all_student = Students.objects.all()
    return render(request, 'student/students-list.html', {'std_list': all_student})
