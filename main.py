from yt_to_audio import yt_to_audio,trim_audio
from speech_to_text import audio_to_txt
from text_analysis import txt_sentiment,sentiment_analysis,df_sentiment
import pandas as pd
# Download a youtube video and extract the audio file
url = 'https://www.youtube.com/watch?v=yYUIt6FtIB4' #Fed Chair Powell speaks at The Brookings Institute on economic outlook — 11/30/22

#yt_to_audio(url)


file_name = 'audio.mp3'
minutes_start = 2
minutes_end = 17.1
out_put_file_name ='trimed_audio.mp3'
# trim audio file
#trim_audio(file_name,out_put_file_name,minutes_start=minutes_start,minutes_end=minutes_end)

# Get the text of the audio file
output = audio_to_txt(out_put_file_name)
output_text = output['text']
segments = output['segments']
df = pd.DataFrame(segments)
df = df[['start','end','text']]


## Checkpoint
# Open the file for writing
# with open('output_text.txt', 'w') as file:
#     # Write the string to the file
#     file.write(output_text)

# # Load txt file into the variable
# output_text = open("output_text.txt", "r")
# output_text = output_text.read()


# Perform text sentiment analysis
sentiments = txt_sentiment(output_text)
df = df_sentiment(df)
df.to_csv('sentiment.csv')
sentiment_analysis(list(df['sentiment']))
#sentiment_analysis(sentiments)

import matplotlib.pyplot as plt
plt.xlabel('Sentences')
plt.show()
