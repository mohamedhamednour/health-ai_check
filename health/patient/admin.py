from django.contrib import admin

# Register your models here.

from .models import Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "date_of_birth", "email")
    search_fields = ("full_name", "email")