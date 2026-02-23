
from django.db import models
from django.db.models import F

class ConsultationQuerySet(models.QuerySet):

    def with_patient_info(self):
        return self.select_related('patient')
    
    def get_info_patient(self):
        return self.annotate(patient_name=models.F('patient__full_name'))
    

    def get_all_info(self):
        return self.with_patient_info().get_info_patient()
