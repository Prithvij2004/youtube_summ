import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

XAI_API_KEY = os.getenv("GROK_API_KEY")

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

def grok(prompt: str):
    completion = client.chat.completions.create(
        model="grok-beta",
        messages=[
            {"role": "system",
                "content": '''
                You are a youtube video summarizer. A detailed generated transcription is provided to you. You have to summarize it
                into short and concise sentences without losing important information. Only use the data provided in the transcription.
                Make you of the transcription fully while answering. Return answer in normal string format with full stops for setence ending.
                '''},
            {"role": "user", "content": f"{prompt}"},
        ],
        temperature=0.2,
    )

    return completion.choices[0].message.content
