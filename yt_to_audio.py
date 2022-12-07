import youtube_dl

# Set the URL of the YouTube video
url = 'https://www.youtube.com/watch?v=yYUIt6FtIB4'

def yt_to_audio(url:str)->None:
    # Set the options for the download and extraction
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'noplaylist': True,
        'playlist-end': 10,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    # Download and extract the audio from the YouTube video
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.cache.remove()
        ydl.download([url])



def trim_audio(input_file_name,out_put_file_name,minutes_start:float=0,minutes_end:float=1)->None :
    # Import the necessary libraries
    from pydub import AudioSegment
    # Load the audio file
    audio = AudioSegment.from_mp3(input_file_name)

    # Cut the first 10 seconds of the audio
    cut_audio = audio[minutes_start*60*1000:minutes_end*60*1000]

    # Export the audio
    cut_audio.export(out_put_file_name, format="mp3")
