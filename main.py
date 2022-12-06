from yt_to_audio import *
from speech_to_text import *
from text_analysis import
# Download a youtube video and extract the audio file
url = 'https://www.youtube.com/watch?v=yYUIt6FtIB4'
file_name = 'audio.mp3'
minutes_start = 2
minutes_end = 17.1
yt_to_audio(url file_name=file_name,minutes_start=minutes_start,minutes_end=minutes_end)

# Get the text of the audio file
output_text = audio_to_txt(file_name)

## Checkpoint
# Open the file for writing
with open('output_text.txt', 'w') as file:
    # Write the string to the file
    file.write(output_text)

# # Load txt file into the variable
# output_text = open("output_text", "r")
# output_text = output_text.read()


# Perform text sentiment analysis
