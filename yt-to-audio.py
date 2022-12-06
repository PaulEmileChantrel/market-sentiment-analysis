import youtube_dl

# Set the URL of the YouTube video
url = 'https://www.youtube.com/watch?v=yYUIt6FtIB4'

def yt_to_audio(url:str,file_name :str = 'audio.mp3',minutes_start:float=0,minutes_end:float=1)->None:
    # Set the options for the download and extraction
    options = {
        'format': 'bestaudio/best',
        'outtmpl': file_name,
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

    # Import the necessary libraries
    from pydub import AudioSegment

    # Set the path to the input audio file
    audio_path = file_name

    # Load the audio file
    audio = AudioSegment.from_mp3(audio_path)

    # Cut the first 10 seconds of the audio
    cut_audio = audio[minutes_start*60*1000:minutes_end*60*1000]
    cut_audio.export(file_name, format="mp3")
