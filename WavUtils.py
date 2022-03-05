#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import pyaudio
import wave

def playWav(filePath) :

	CHUNK = 1024

	wf = wave.open(filePath, 'rb')

	data = wf.readframes(CHUNK)

	p = pyaudio.PyAudio()


	FORMAT = p.get_format_from_width(wf.getsampwidth())
	CHANNELS = wf.getnchannels()
	RATE = wf.getframerate()

	print('FORMAT: {} \nCHANNELS: {} \nRATE: {}'.format(FORMAT, CHANNELS, RATE))

	stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,frames_per_buffer=CHUNK,output=True)
	while len(data) > 0:
		stream.write(data)
		data = wf.readframes(CHUNK)
