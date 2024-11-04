import subprocess
import sys
import os

def run_combined_scripts(video_id, output_file='script.txt'):
    print(f"Processing video ID: {video_id}")
    
    # Check if scripts exist
    if not os.path.exists('ytr.py'):
        print("Error: ytr.py not found")
        return
    if not os.path.exists('sumarize.py'):
        print("Error: sumarize.py not found")
        return
    
    # First command: python ytr.py VIDEO_ID -o script.txt
    print("\nStep 1: Extracting transcript...")
    try:
        result = subprocess.run(
            ['python', 'ytr.py', video_id, '-o', output_file],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running ytr.py: {e}")
        print(f"Error output: {e.stderr}")
        return
    
    # Check if output file was created
    if not os.path.exists(output_file):
        print(f"Error: {output_file} was not created")
        return
    
    # Second command: python summarize.py script.txt
    print("\nStep 2: Generating summary...")
    try:
        result = subprocess.run(
            ['python', 'sumarize.py', output_file],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running sumarize.py: {e}")
        print(f"Error output: {e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py VIDEO_ID")
        print("Example: python run.py aj0S55-aXjQ")
        sys.exit(1)
    
    video_id = sys.argv[1]
    run_combined_scripts(video_id)
    print("\nProcess completed!")