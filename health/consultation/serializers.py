from rest_framework import serializers
from .models import Consultation



class ConsultationSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(read_only=True)
    class Meta:
        model = Consultation
        fields =   "__all__"
    