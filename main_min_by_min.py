from yt_to_audio import *
from speech_to_text import *
from text_analysis import *

# Download a youtube video and extract the audio file
url = 'https://www.youtube.com/watch?v=yYUIt6FtIB4' #Fed Chair Powell speaks at The Brookings Institute on economic outlook — 11/30/22

file_name = 'audio.mp3'
minutes_start = 2
minutes_end = 17.1
yt_to_audio(url)
sentiment_per_min = []
for i in range(int(minutes_start),round(minutes_end+0.5)):

    out_put_file_name ='minute_trimed/trimed_audio'+str(i)+'.mp3'
    # trim audio file
    trim_audio(file_name,out_put_file_name,minutes_start=i,minutes_end=i+1)

    # Get the text of the audio file
    output_text = audio_to_txt(out_put_file_name)

    # Perform text sentiment analysis
    sentiment_per_min.append(txt_overall_sentiment(output_text)[0])
    print(sentiment_per_min)
print(sentiment_per_min)
sentiment_analysis(sentiment_per_min)

import matplotlib.pyplot as plt
plt.xlabel('Speech (in minutes)')
plt.show()
