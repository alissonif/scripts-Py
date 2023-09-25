# Importando o módulo Pillow (Manipulação de Imagens) para abrir a imagem no script
from py_translate import Translator
from PIL import Image
# Módulo para a utilização da tecnologia OCR
import pytesseract
# Extraindo o texto da imagem
print(pytesseract.image_to_string(Image.open(
    './1.png')))
