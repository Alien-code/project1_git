from django.shortcuts import render
from .models import SchoollInfo

# Create your views here.


def school_list(request):
    school_list = SchoollInfo.objects.all()
    return render(request, 'school/school-list.html', {'school_list': school_list})


def school_details(request, school_id):
    school = SchoollInfo.objects.get(pk=school_id)
    return render(request, 'school/school_details.html', {'school': school})
