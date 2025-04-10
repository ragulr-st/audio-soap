from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from transcription import transcribe_audio
from soap_generator import generate_soap_note
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# 👇 Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class TranscriptRequest(BaseModel):
    transcript: str = Field(
        ..., 
        example="Patient reports chest pain while exercising.",
        description="Transcript of patient conversation to generate SOAP note"
    )


@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    if not file.filename.endswith(('.mp3', '.wav')):
        raise HTTPException(status_code=400, detail="Invalid file format")
    
    text = await transcribe_audio(file)
    return {"transcript": text}


@app.post("/generate-soap")
def generate_soap_endpoint(data: TranscriptRequest):
    soap_note = generate_soap_note(data.transcript)
    return {"soap_note": soap_note}


@app.post("/audio-to-soap")
async def audio_to_soap(file: UploadFile = File(...)):
    if not file.filename.endswith(('.mp3', '.wav')):
        raise HTTPException(status_code=400, detail="Only .mp3 or .wav files are supported")

    # Step 1: Transcribe the audio
    transcript = await transcribe_audio(file)
    # Step 2: Generate the SOAP note
    soap_note = generate_soap_note(transcript)

    return {
        "transcript": transcript,
        "soap_note": soap_note
    }