import whisper


def audio_to_txt(audio_file:str)->str:
    # Whisper
    model = whisper.load_model("base")
    result = model.transcribe(audio_file,verbose=True)
    # print(result)
    # print(result["text"])
    return result
