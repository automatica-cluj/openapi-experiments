from pathlib import Path
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="API-KEY")

# Define the text-to-speech input as a multiline string
input_text = """First line of the speech.
- Second line of the speech.
- Third line of the speech.
"""

model = "tts-1"
voice = "alloy"

# Define the output file path
speech_file_path = Path(__file__).parent / "speech.mp3"

# Generate the speech
try:
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=input_text
    )
    # Save the generated speech to a file
    response.stream_to_file(speech_file_path)
    print(f"Speech saved to {speech_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
