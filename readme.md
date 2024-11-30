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

### Running the Server

Start the FastAPI server:
```sh
fastapi dev main.py