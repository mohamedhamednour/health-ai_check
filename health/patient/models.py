import uuid
from django.db import models


class Patient(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    full_name = models.CharField(
        max_length=255
    )
    date_of_birth = models.DateField()
    email = models.EmailField(
        unique=True
    )

    def __str__(self):
        return self.full_name