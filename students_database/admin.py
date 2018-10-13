from django.contrib import admin
from .models import Guardian
from .models import Students

# Register your models here.
admin.site.register(Guardian)
admin.site.register(Students)
