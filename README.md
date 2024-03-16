# Voice-Activated Wikipedia/Google Search Tool

## Description
This Python script allows users to search Wikipedia using their voice. It utilizes speech recognition to transcribe the user's speech, queries Wikipedia for the recognized input, and reads a summary of the corresponding article aloud using text-to-speech capabilities.

## Features
- Voice-activated input for searching Wikipedia.
- Speech recognition using Google's speech recognition API.
- Text-to-speech functionality to read Wikipedia article summaries aloud.

## Dependencies
- Python 3.x
- pyttsx3
- wikipedia
- speech_recognition

## Installation
1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required dependencies using pip:
    ```
    pip install pyttsx3 wikipedia SpeechRecognition
    ```
3. Clone or download the script file (`wikipedia_search.py`) from this repository.

## Usage
1. Run the script using Python:
    ```
    python wikipedia_search.py
    ```
2. Allow the script to access your microphone when prompted.
3. Speak your query clearly into the microphone.
4. Wait for the script to process your speech and read the summary of the Wikipedia article aloud.

## Example
Suppose you want to search for information about Albert Einstein on Wikipedia:
1. Run the script.
2. Speak "Albert Einstein" clearly into the microphone.
3. The script will recognize your speech, query Wikipedia, and read a summary of Albert Einstein's Wikipedia article aloud.

## Contributors
- [Your Name](https://github.com/kattavignesh)


## Acknowledgments
- Special thanks to the developers of pyttsx3, wikipedia, and SpeechRecognition for their valuable contributions.

