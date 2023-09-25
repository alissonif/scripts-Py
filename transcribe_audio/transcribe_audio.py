import librosa
import soundfile
import speechrecognition as sr


def remove_noise(audio_file):
    """Remove ruído do áudio.

    Args:
      audio_file: O arquivo de áudio.

    Returns:
      O áudio sem ruído.
    """

    # Carrega o áudio.
    audio, sr = librosa.load(audio_file, sr=16000)

    # Aplica um filtro passa-baixas para remover ruído de baixa frequência.
    audio = librosa.filter(audio, 0, 8000)

    # Aplica um filtro passa-altas para remover ruído de alta frequência.
    audio = librosa.filter(audio, 8000, None)

    # Recorta o áudio para remover silêncios no início e no fim.
    audio = librosa.effects.trim(audio)

    return audio


def transcribe_audio(audio_file):
    """Transcreve o áudio em texto.

    Args:
      audio_file: O arquivo de áudio.

    Returns:
      O texto transcrito.
    """

    # Remove o ruído do áudio.
    audio = remove_noise(audio_file)

    # Cria um reconhecedor de fala.
    recognizer = sr.Recognizer()

    # Transcreve o áudio.
    with soundfile.SoundFile(audio_file) as f:
        audio = f.read()
        transcript = recognizer.recognize_google(audio)

    return transcript


if __name__ == "__main__":
    # Especifica o arquivo de áudio.
    audio_file = "audio.wav"

    # Transcreve o áudio.
    transcript = transcribe_audio(audio_file)

    # Imprime a transcrição.
    print(transcript)
