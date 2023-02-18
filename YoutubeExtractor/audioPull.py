from pytube import YouTube

def download_audio(url):
    # Create a YouTube object
    yt = YouTube(url)

    # Get the audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream
    output_filename = f"{yt.title}.mp3"
    audio_path = audio_stream.download(output_path='C:/Users/jor72/Downloads/', filename=output_filename)

    return audio_path