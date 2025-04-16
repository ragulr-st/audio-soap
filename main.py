from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from transcription import transcribe_audio
from soap_generator import generate_soap_note
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

ALLOWED_AUDIO_EXTENSIONS = ('.mp3', '.wav', '.m4a', '.webm', '.mp4', '.ogg', '.flac')

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

def is_valid_audio_file(filename: str) -> bool:
    return filename.lower().endswith(ALLOWED_AUDIO_EXTENSIONS)


@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    if not is_valid_audio_file (file.filename):
        raise HTTPException(status_code=400, detail="Invalid file format")
    
    text = await transcribe_audio(file)
    return {"transcript": text}


@app.post("/generate-soap")
def generate_soap_endpoint(data: TranscriptRequest):
    soap_note = generate_soap_note(data.transcript)
    return {"soap_note": soap_note}


@app.post("/audio-to-soap")
async def audio_to_soap(file: UploadFile = File(...)):
    if not is_valid_audio_file (file.filename):
        raise HTTPException(status_code=400, detail="Only .mp3 or .wav files are supported")

    # Step 1: Transcribe the audio
    transcript = await transcribe_audio(file)
    # Step 2: Generate the SOAP note
    soap_note = generate_soap_note(transcript)

    return {
        "transcript": transcript,
        "soap_note": soap_note
    }