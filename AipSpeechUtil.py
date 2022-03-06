# -*- coding:utf-8 -*-
from utils import *

APP_ID = '25709228'
API_KEY = 'oOUMpGrZzj71M6F4MlZavOD2'
SECRET_KEY = 'xprrvxGX5VmthpIbZMtRfQAjxUxQ0EBC'

def textToWav(content, outputPath):
	import subprocess
	import shlex
	from aip import AipSpeech

	aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
	print ("\ttextToWav %s..."%(content[0:10]))
	result = aipSpeech.synthesis(content, 'zh', 1, {'vol': 5,'per':5003})
	if not isinstance(result, dict):
	    with open(outputPath, 'ab+') as f:
	        f.write(result)


def getAppleVoicenames():
    from  AppKit import NSSpeechSynthesizer

    """I am returning the names of the voices available on Mac OS X."""
    voices = NSSpeechSynthesizer.availableVoices()
    voicenames = []
    for voice in voices:
        voiceattr = NSSpeechSynthesizer.attributesForVoice_(voice)
        voicename = voiceattr['VoiceName']
        if voicename not in voicenames:
            voicenames.append(voicename)
    return voicenames

def combineAudio(destPath, fromPath, format_v):
	from pydub import AudioSegment
	if not fileExist(destPath):
		myaudio1 = AudioSegment.from_file(fromPath)
		output_audio =  myaudio1
		output_audio.export(destPath)
	else:
		myaudio0 = AudioSegment.from_file(destPath)
		myaudio1 = AudioSegment.from_file(fromPath)

		output_audio = myaudio0 + myaudio1
		output_audio.export(destPath, format = format_v, bitrate='192k')


def tts_nsss(content, outputPath, format = "wav"):
	from  AppKit import NSSpeechSynthesizer
	import sys
	import Foundation

	tempPath = "./temp." + format
	text = content

	nssp = NSSpeechSynthesizer
	ve = nssp.alloc().init()
	ve.setRate_(200)
	ve.setVoice_('com.apple.speech.synthesis.voice.Mei-Jia')
	url = Foundation.NSURL.fileURLWithPath_(tempPath)
	ve.startSpeakingString_toURL_(text,url)
	# ve.continueSpeakingString_toURL_(text,url)

	combineAudio(outputPath, tempPath, format)

# tts_nsss("","")
