import speech_recognition as sr


def extract_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-US')
        return text


audio_file = './The-Weeknd-will.i.am-Boys-Girls-ft.-Pia-Mia.wav'
text = extract_text(audio_file)
print(text)
