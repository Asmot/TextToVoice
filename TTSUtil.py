# -*- coding:utf-8 -*-
from utils import *
from role import *
from TTS_MacApple import *
from TTS_Baidu import *

class TextDurationItem :
	start = 0
	duration = 0
	text = ""

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

## 根据角色选择不同的语音
def tts_switch_by_role(textItem, tempPath, role):
	if role == SegmentRole_VoiceOver:
		flag = tts_apple(textItem, tempPath)
	elif role == SegmentRole_Person: 
		flag = tts_apple(textItem, tempPath)
	else:
		flag = tts_apple(textItem, tempPath)
	return flag;
	
# 返回这段文本的播放时长 单位 s, 返回数组
# 如果content有标点符号会被拆分为多个，按照中文标点符号拆分
def tts_role(content, outputPath, format = "wav", role = SegmentRole_VoiceOver):
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

		deleteFile(tempPath)
		flag = tts_switch_by_role(textItem, tempPath, role)
		if not flag:
			return False

		combineAudio(outputPath, tempPath, format)

		finalDuration = getAudioTime(outputPath)
	
		# 避免拼接出现异常 使用前后评接时长的查值
		item = TextDurationItem()
		item.text = textItem;
		item.start = beforeDuration;
		item.duration = (finalDuration - beforeDuration)
		resultItems.append(item)
	return resultItems


if __name__ == "__main__":	
	result = getAppleVoicenames()
	voices = ['com.apple.speech.synthesis.voice.Mei-Jia','com.apple.speech.synthesis.voice.Ting-Ting']
	for voice in voices:
		outputPath = "./output/" + voice + ".wav"
		tts_nsss("测试abc", outputPath, "wav", voice)

# tts_nsss("","")
