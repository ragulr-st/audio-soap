import os
import tempfile
import whisper

model = whisper.load_model("base")

async def transcribe_audio(file):
    # Extract the file extension from the uploaded filename
    _, ext = os.path.splitext(file.filename)
    ext = ext.lower()

    # Create a temp file with the correct extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    try:
        result = model.transcribe(tmp_path)
        return result['text']
    finally:
        os.remove(tmp_path)