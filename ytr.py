from youtube_transcript_api import YouTubeTranscriptApi
import re
import sys
import argparse

def extract_video_id(video_url_or_id):
    """
    Extract video ID from a YouTube URL or return the ID if already provided
    """
    if 'youtube.com' in video_url_or_id or 'youtu.be' in video_url_or_id:
        video_id_match = re.search(r'(?:v=|youtu\.be/)([^&]+)', video_url_or_id)
        if not video_id_match:
            raise ValueError("Could not extract video ID from URL")
        return video_id_match.group(1)
    return video_url_or_id

def get_youtube_transcript(video_url_or_id):
    """
    Retrieve the transcript of a YouTube video.
    
    Args:
        video_url_or_id (str): YouTube video URL or video ID
        
    Returns:
        str: Full transcript text
        
    Raises:
        ValueError: If video ID cannot be extracted or transcript is unavailable
    """
    try:
        video_id = extract_video_id(video_url_or_id)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([entry['text'] for entry in transcript_list])
        return transcript_text
    except Exception as e:
        raise ValueError(f"Could not retrieve transcript: {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Get YouTube video transcript')
    parser.add_argument('video', help='YouTube video URL or ID')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Get transcript
        transcript = get_youtube_transcript(args.video)
        
        # Handle output
        if args.output:
            # Save to file
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(transcript)
            print(f"Transcript saved to {args.output}")
        else:
            # Print to console
            print("\nTranscript:")
            print("-----------")
            print(transcript)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()