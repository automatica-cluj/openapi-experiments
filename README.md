# YT video summarizer

## Introduction
This program uses the OpenAI API to generate a summary of the video transcript. You need to set your OpenAI API key (https://platform.openai.com/settings/organization/api-keys) in the `sumarize.py` file.

The program use preexisting transcript from YouTube video. If the video does not have a transcript, the program will not work.

## Dependencies
To run the program, you need to install the following libraries:

1. `youtube_transcript_api`
2. `openai`

You can install these libraries using `pip`. Here are the steps:

1. Open a terminal or command prompt.
2. Run the following commands:

```sh
pip install youtube_transcript_api
pip install openai
```

## Usage

To run the program, use the following command:

```sh
python run.py VIDEO_ID
```

Replace `VIDEO_ID` with the actual YouTube video ID you want to process.

Example:

```sh
python run.py aj0S55-aXjQ
```

```
Processing video ID: aj0S55-aXjQ

Step 1: Extracting transcript...
Transcript saved to script.txt


Step 2: Generating summary...
Summary:
 In this meeting, the speaker discusses the disassembly and reassembly of an Olympus OM F SU ECO Auto S 50mm 1.8 lens. The lens is described as relatively easy to disassemble, but with some complexities that make repairs more challenging, particularly due to the coupling of the diaphragm with mechanical parts.

Key points discussed include:

1. **Disassembly Process**:
   - The speaker begins by removing the aperture control ring and accessing the diaphragm and front optics.
   - They explain the need for specific tools, such as a pointed tip spanning wrench, and demonstrate how to remove various rings and components carefully to avoid damaging mechanical parts.
   - The diaphragm mechanism is highlighted as a single piece that complicates cleaning and repair.

2. **Mechanical Components**:
   - The speaker details the removal of the mounting plate and the back optics, emphasizing the importance of understanding how the aperture control and stop-down mechanisms work together.
   - They mention optional steps for disassembly, particularly regarding parts that may not need to be removed unless mechanical issues arise.

3. **Reassembly Challenges**:
   - The reassembly process is described as more complex due to the need for precise alignment of various components, especially the diaphragm and mechanical parts.
   - The speaker provides instructions on how to ensure proper coupling of the aperture control mechanism during reassembly.

4. **Final Thoughts**:
   - The speaker concludes that while the lens is repairable, its design presents certain difficulties that require careful attention during both disassembly and reassembly.

Overall, the meeting serves as a detailed guide for handling the Olympus lens, focusing on the intricacies involved in its repair process.


Process completed!

```