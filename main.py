from fastapi import FastAPI

from utils.transcript import get_transcription
from utils.summarize import grok

app = FastAPI()

@app.get("/transcript")
async def transcription(video_id: str):
    transcript = get_transcription(video_id)
    return {"transcript": transcript}

@app.get("/summarize")
async def summarize(video_id: str):
    transcript = get_transcription(video_id)
    summary = grok(transcript)
    return {"summary": summary}