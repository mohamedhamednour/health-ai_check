from ast import Dict
import os
import django
import uuid

# Initialize Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from asgiref.sync import sync_to_async
from fastmcp import FastMCP 
from consultation.models import Consultation
mcp = FastMCP("consultation_service")


import json

@mcp.tool()
async def get_consultation(consultation_id: str) -> Dict:
    """Search for a consultation using its unique identifier """
    
    try:
        c_id = uuid.UUID(consultation_id)
    except ValueError:
        return f"Invalid UUID format: {consultation_id}"

    # Use sync_to_async for DB operations
    get_consultation_obj = sync_to_async(
        lambda: Consultation.objects.select_related('patient').filter(id=c_id).first()
    )
    consultation = await get_consultation_obj()

    if not consultation:
        return f"Consultation with ID {consultation_id} not found."

    return {
        "consultation_id": str(consultation.id),
        "patient_name": consultation.patient.full_name,
        "patient_email": consultation.patient.email,
        "symptoms": consultation.symptoms,
        "existing_diagnosis": consultation.diagnosis or 'None',
        "created_at": consultation.created_at.isoformat()      
    }

if __name__ == "__main__":
    mcp.run()