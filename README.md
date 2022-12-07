# Market sentiment analysis

Download a video from youtube and perform a sentiment analysis on its audio.


### Step 1

Download a video from Youtube and extract the audio.
Trim the audio if necessary.

### Step 2

Use `whisper` to perform audio-to-text transription.

## Step 3 

Use a transformer to perform the sentiment analysis on every sentence.

Here is the sentiment during the speech (0% is totally negative and 100% is totally positive) :
<p align='center'>
<img src='https://user-images.githubusercontent.com/96018383/206060639-5341d8d5-77cc-4518-8ade-de93c42f2b18.png'>
</p>



## Version 2: minute by minute analysis

We are doing a similar process except we split the audio file every minute and perform a transcribe and analysis on each piece.

<p align='center'>
<img src='https://user-images.githubusercontent.com/96018383/206049334-e37804d2-8241-430d-9c06-c778df7d75fd.png'>
</p>

