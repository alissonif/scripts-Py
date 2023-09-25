import webbrowser

# Lista de URLs dos sites de notícias
news_urls = [
    'https://docs.google.com/document/d/1XrCPuGPsbu9SY1boDUofAKr9SlwcgxD5Agt2XGRH_2Q/edit?usp=sharing',
    'https://www.linkedin.com/in/josealissonif/',
    'https://github.com/alissonif'
    'https://app.rocketseat.com.br/me/josealisson'
]

# Abre cada URL em uma nova aba do navegador
for url in news_urls:
    webbrowser.open_new_tab(url)
