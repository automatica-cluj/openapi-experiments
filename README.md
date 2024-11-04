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
