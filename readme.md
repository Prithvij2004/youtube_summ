# YouTube Video Summarizer

This project provides a FastAPI-based service to transcribe and summarize YouTube videos. It uses the `youtube_transcript_api` to fetch video transcripts and the OpenAI API to generate summaries.

## Project Structure


## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a `.env` file and add your Grok API key:
    ```
    GROK_API_KEY=your_openai_api_key
    ```

## Usage
1. Go to localhose:8000/docs for the FastAPI Swagger UI docs.
2. Enter the YouTube video id and click the "Summarize" button.
3. For a video with url "https://www.youtube.com/watch?v=RH7REzcVjMI&ab_channel=AliAbdaal", the video id is "RH7REzcVjMI".
Note: Will add method to use video url directly.
Note: There is no audio downloading and audio -> transcript conversion. The video transcript is fetched directly from the youtube-transcript-api. Will add technique for audio -> transcript conversion if directly not available.

### Running the Server

Start the FastAPI server:
```sh
fastapi dev main.py