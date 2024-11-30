from youtube_transcript_api import YouTubeTranscriptApi

def get_transcription(video_id: str):
    raw_transcription = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = " ".join([line["text"] for line in raw_transcription])
    return {"transcript": transcript}
