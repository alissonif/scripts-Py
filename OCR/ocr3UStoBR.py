import googletrans

# Abre a imagem do manga
image = cv2.imread("manga.jpg")

# Extrai o texto da imagem
text = pytesseract.image_to_string(image)

# Traduz o texto para o português
translation = googletrans.translate(text, src="en", dest="pt")

# Imprime a tradução
print(translation)
