from django.db import models
import uuid

from patient.models import Patient
from .manger import ConsultationQuerySet
class Consultation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="consultations"
    )
    symptoms = models.TextField()
    diagnosis = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    ai_summary = models.TextField(
        blank=True,
        null=True
    )
    objects = ConsultationQuerySet.as_manager()

    def __str__(self):
        return f"Consultation for {self.patient.full_name} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"