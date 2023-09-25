import whisper
modelo = whisper.load_model('base')
resposta = modelo.transcribe('Gravando.m4a')
print(resposta['text'])