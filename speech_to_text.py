import openai
import os

def audio_to_txt(audio_file:str)->str:
    # Set your API key
    openai.api_key = os.environ['OPEN_AI_API_KEY']

    # Choose the audio file you want to convert to text
    #audio_file = "audio.mp3"

    # Use the speech_to_text method with the whisper model and set the temperature and timestamps arguments
    response = openai.speech_to_text(
        audio=audio_file,
        model="text-davinci-003",
        temperature=0.5,
        timestamps=True,
    )

    # Print the generated transcript with timestamps
    print(response["text"])
    return response["text"]
