from django.contrib import admin

# Register your models here.

from .models import Consultation
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("patient", "created_at")
    search_fields = ("patient__full_name",)
    list_filter = ("created_at",)