import openai
import os

def audio_to_txt(text:str):
    # Set your API key
    openai.api_key = os.environ['OPEN_AI_API_KEY']

    # Use the classify_text method to perform sentiment analysis
    response = openai.classify_text(
        prompt=text,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )

    # Print the predicted classes and probabilities
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]
