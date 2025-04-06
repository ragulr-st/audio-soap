import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Ensure the API key is fetched securely
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)

def generate_soap_note(transcript: str) -> str:
    """
    Generates a SOAP note based on a given patient transcript.
    """
    response = client.chat.completions.create(
        model="gpt-4",  # Or "gpt-3.5-turbo" if you're using that
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a compassionate and detail-oriented primary care medical assistant responsible "
                    "for generating comprehensive and well-structured SOAP (Subjective, Objective, Assessment, Plan) "
                    "notes from patient-provider encounter transcripts. Your goal is to accurately reflect the clinical "
                    "interaction, including the patient’s reported symptoms, the provider’s observations, clinical assessments, "
                    "and the care plan discussed during the visit. Ensure that medical terminology is used appropriately, "
                    "all relevant details are included, and the tone remains professional and clear for integration into the "
                    "patient’s electronic health record (EHR)."
                )
            },
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content
