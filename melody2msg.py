#!/usr/bin/python
# -*- coding: utf-8 -*-
# Aron Galdon
# 2017/04/07
# melody2msg.py

import sys
import multiprocessing as mp
import time
import pyaudio
import numpy as np

CHUNK = 128
CHANNELS = 1
RATE = 22050
DELAY_SIZE = 1


def feed_queue(q):

    FORMAT = pyaudio.paInt16
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    while True:
        frame = []
        for i in xrange(10):
            frame.append(stream.read(CHUNK))
        data_ar = numpy.fromstring(''.join(frame), 'int16')
        if q.full():
            q.get_nowait()
        q.put(data_ar)

def main(argv):
    """
    Función principal.

    """
    queue = mp.Queue(maxsize=DELAY_SIZE)
    p = mp.Process(target=feed_queue, args=(queue,))

    raw_input("Pulse Enter para empezar a escuchar...")
    p.start()

    for t in range(0, 99):
        t += 1
        d = queue.get()




# Inicio del programa
if __name__ == '__main__':
    main(sys.argv)
