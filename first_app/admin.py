from django.contrib import admin
from first_app.models import category,location,doctor,Appointments

admin.site.register(category)
admin.site.register(location)
admin.site.register(doctor)
admin.site.register(Appointments)

# Register your models here.
