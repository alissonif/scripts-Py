import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
import sys

path="./The Weeknd-will.i.am - Boys  Girls ft. Pia Mia.mp3"

clip=mp.VideoFileClip(path).subclip()

clip.audio.write_audiofile("audio.mp3")

audio=AudioSegment.from_file("audio.mp3")

size=180000

chunks=make_chunks(audio, size)

for i, chunk in enumerate(chunks):
    chunk_name="audio{0}.wav".format(i)

    chunk.export(chunk_name, format="wav")
    file_audio=sr.AudioFile("./"+chunk_name)

    r=sr.Recognizer()

    with file_audio as source:
        audio_text=r.record(source)
        text=r.recognize_google(audio_text, language="pt-BR")
    arquivo=open(chunk_name.replace(".wav","")+'.txt','w')
    arquivo.write(text)
    arquivo.close()
    print(text)