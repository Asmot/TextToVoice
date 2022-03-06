# -*- coding:utf-8 -*-
from utils import *

APP_ID = '25709228'
API_KEY = 'oOUMpGrZzj71M6F4MlZavOD2'
SECRET_KEY = 'xprrvxGX5VmthpIbZMtRfQAjxUxQ0EBC'

class TextDurationItem :
	start = 0
	duration = 0
	text = ""

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
		output_audio.export(destPath, format = format_v, bitrate='192k')
	else:
		myaudio0 = AudioSegment.from_file(destPath)
		myaudio1 = AudioSegment.from_file(fromPath)

		output_audio = myaudio0 + myaudio1
		output_audio.export(destPath, format = format_v, bitrate='192k')

## 单位 s
def getAudioTime(filePath):
	if not fileExist(filePath):
		return 0;

	from pydub import AudioSegment
	myaudio1 = AudioSegment.from_file(filePath)
	return len(myaudio1)  / 1000

	
# 返回这段文本的播放时长 单位 s, 返回数组
# 如果content有标点符号会被拆分为多个，按照中文标点符号拆分
def tts_nsss(content, outputPath, format = "wav"):
	from  AppKit import NSSpeechSynthesizer
	import sys
	import Foundation

	tempPath = "./temp." + format
	text = content

	resultItems = []
	
	textList = splitWords(text)
	
	for textItem in textList:
		# print ("text: %s textLen %s"%(textItem, len(textItem)))
		if len(textItem) == 0:
			continue

		# 获取时长
		beforeDuration = getAudioTime(outputPath)
		# print ("before duration " + str(beforeDuration))

		nssp = NSSpeechSynthesizer
		ve = nssp.alloc().init()
		ve.setRate_(200)
		ve.setVoice_('com.apple.speech.synthesis.voice.Mei-Jia')
		url = Foundation.NSURL.fileURLWithPath_(tempPath)
		ve.startSpeakingString_toURL_(textItem, url)
		# ve.continueSpeakingString_toURL_(text,url)
		combineAudio(outputPath, tempPath, format)

		finalDuration = getAudioTime(outputPath)
	
		# 避免拼接出现异常 使用前后评接时长的查值
		item = TextDurationItem()
		item.text = textItem;
		item.start = beforeDuration;
		item.duration = (finalDuration - beforeDuration)
		resultItems.append(item)
	return resultItems




# tts_nsss("","")
