from rest_framework import viewsets, status , mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from llm.agent.handler_ai_summary import HandlerAISummary

from .models import Consultation
from .serializers import ConsultationSerializer

class ConsultationViewSet( mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Consultation.objects.all().get_all_info()
    serializer_class = ConsultationSerializer

    @action(detail=True, methods=["post"])
    def generate_summary(self, request, pk=None):
        consultation = get_object_or_404(Consultation, pk=pk)

        if not consultation.symptoms:
            return Response(
                {"error": "Symptoms are required to generate summary."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Call AI service
        handler_ai_summary = HandlerAISummary(consultation.id)
        from asgiref.sync import async_to_sync
        summary = async_to_sync(handler_ai_summary.handle_llm)()
        consultation.ai_summary = summary
        consultation.save()
        serializer = self.get_serializer(consultation)
        return Response(serializer.data, status=status.HTTP_200_OK)