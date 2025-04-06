# 🩺 Audio to SOAP Note - FastAPI App

This is a simple FastAPI-based application that lets you upload an audio file (e.g., `.mp3` or `.wav`) containing a patient transcript and get a structured SOAP note using OpenAI.

---

## 📦 Features

- Upload audio and transcribe to text using Whisper
- Convert transcribed text to a SOAP note using OpenAI API
- REST API endpoints documented with Swagger UI
- Dockerized for easy deployment

---

## 🛠️ Prerequisites

### Install Docker

#### macOS (using Homebrew)
```bash
brew install --cask docker
open /Applications/Docker.app
```

- Wait for Docker to start (check top menu bar)
- Test it works:
```bash
docker --version
```

---

## 🚀 Run the App

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/audio-soap-backend.git
cd audio-soap-backend
```

### 2. Build Docker Image
```bash
docker build -t fastapi-audio-soap .
```

### 3. Run the Docker Container
```bash
docker run -d -p 8000:8000 fastapi-audio-soap
```

### 4. Open API Docs in Browser
```
http://localhost:8000/docs
```

Use `/upload-audio` to upload audio and get transcript.  
Use `/generate-soap` to generate SOAP note from transcript.

---

## 🔄 Make Changes

Edit code in the project folder, then:

1. Stop running containers:
```bash
docker ps
docker stop <container_id>
```

2. Rebuild image:
```bash
docker build -t fastapi-audio-soap .
```

3. Run again:
```bash
docker run -d -p 8000:8000 fastapi-audio-soap
```

---

## 🧪 API Endpoints

| Method | Endpoint         | Description                      |
|--------|------------------|----------------------------------|
| POST   | `/upload-audio`  | Upload audio & get transcript    |
| POST   | `/generate-soap` | Generate SOAP note from transcript |

---

## 🔐 Environment Variables

Your OpenAI key is used directly in `soap_generator.py`. You can later change this to use `.env`.

---

## 📁 Project Structure

```
audio-soap-backend/
│
├── main.py                 # FastAPI app
├── transcription.py        # Audio to text logic
├── soap_generator.py       # Transcript to SOAP note logic
├── requirements.txt
├── Dockerfile
└── README.md               # You're here
```

---

## ✅ To Do

- [ ] Add `.env` for secret management
- [ ] Add frontend UI for easier testing
- [ ] Add tests

---

## 📬 Need Help?

Feel free to raise an issue or ping me!

---

## 🧠 About SOAP Notes

**SOAP** = Subjective, Objective, Assessment, Plan  
It’s a format for documenting patient information.

---

## 🔗 License

MIT