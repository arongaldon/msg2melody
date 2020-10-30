#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Aron Galdon Gines
# 2017/04/07 First version on Python 2
# 2020/10/30 Migration to Python 3
# msg2melody.py mensaje

import sys
import math
import pyaudio # C:\Python27\scripts\pip install pyaudio

# Calidad: bits por segundo
BITRATE = 22050     

# Tono musical base en Hz
FREC_BASE = 8.13

# Duración del tono en segundos
DURACION = 3

def generar_tono(n):
    datos_onda = ''
    nframes = int(BITRATE * DURACION)
    for x in range(nframes):
        a = FREC_BASE * n
        b = (BITRATE / a) / math.pi
        c = x / b
        valor = int(math.sin(c) * 127 + 128)
        datos_onda = datos_onda + chr(valor)    

    resto = nframes % BITRATE
    for x in range(resto): 
        datos_onda = datos_onda + chr(128)

    return datos_onda



def main(argv):
    """
    Función principal.

    """
    if not argv[1:]: 
        argv.append('abc')

    input("Pulse Enter para empezar a reproducir...")
    audio = ''
    for c in argv[1]:
        n = ord(c)
        print ('{0} {1}'.format(c, n))
        audio = audio + generar_tono(n)

    PyAudio = pyaudio.PyAudio
    p = PyAudio()
    stream = p.open(
        format = p.get_format_from_width(1), 
        channels = 1, rate = BITRATE, output = True)

    stream.write(audio)
    stream.stop_stream()
    stream.close()
    p.terminate()

# Inicio del programa
if __name__ == '__main__':
    main(sys.argv)
