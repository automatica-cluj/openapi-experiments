import openai
from openai import OpenAI
import sys

# Replace with your OpenAI API key
openai.api_key = "[YOUR-API-KEY]"


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="YOUR-API-KEY",
)

# Check if the filename argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <transcript_filename>")
    sys.exit(1)

# Get the filename from command-line arguments
transcript_filename = sys.argv[1]

# Define a function to load the transcript from a file
def load_transcript(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

# Define a function to summarize the transcript
def summarize_transcript(transcript_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes meeting transcripts."},
            {"role": "user", "content": "Summarize the following meeting transcript: " + transcript_text}
        ],
        temperature=0.5,
    )
    
    # Access the assistant's summary from the response
    summary = response.choices[0].message.content
    return summary

# Load the transcript text from the specified file
transcript_text = load_transcript(transcript_filename)

# Run the function and print the summary
summary = summarize_transcript(transcript_text)
print("Summary:\n", summary)