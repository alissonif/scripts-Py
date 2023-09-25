from pytesseract import pytesseract

caminho_tesseract = "/usr/bin/tesseract"

pytesseract.tesseract_cmd = caminho_tesseract
texto = pytesseract.image_to_string(
    './1.png')

# print(texto)

linhas = texto.split('\n')

for linha in linhas:
    if not linha.isspace() and len(linha) > 0:
        print(linha)
