#!/usr/bin/python
# -*- coding: UTF-8 -*-

from utils import *

from TextSegment import *
from TTSUtil import *
from VideoUtils import *

AUDIO_FORMAT = "wav"
TD_FORMAT = "td"
MOVIE_FORMAT = "mp4"

def getAllFiles(dir):
	fileNames = listFiles(dir)
	total_len = len(fileNames)

	result = []
	## filter by 第 n 章
	PRE_STR = "第%s章"
	for i in range(0, total_len + 1):
		fileNamePre = PRE_STR%(i)
		for name in fileNames:
			if fileNamePre in name:
				result.append(name)
				break
	return result

## 生成语音和字幕文件
## 字幕文件以td结尾 内容是 文本和时长，换行分割
def tts_to_file(filePath, outputPath, outputTdPath):
	outputPathTextDuration = outputTdPath
	print (filePath + " => " + outputPath)
	fileCon = readFile(filePath)
	## text to words segments

	index = 0;
	segments = textToSegmentByLines(fileCon)
	totalLen = len(segments)
	for seg in segments:
		# 如果words有标点符号会被拆分为多个
		tdItems = tts_role(seg.words, outputPath, AUDIO_FORMAT, seg.role);
		for tdItem in tdItems:
			print ("保存字幕: %.2f, %.2f text %s"%(tdItem.start, tdItem.duration, tdItem.text))

			# 保存文本和文本播放时长，用来制作字幕
			writeFileAppend(outputPathTextDuration, tdItem.text)
			if not tdItem.text.endswith("\n"):
				# 保证换行
				writeFileAppend(outputPathTextDuration, "\n")
				
			writeFileAppend(outputPathTextDuration, str(tdItem.start) + "\n")
			writeFileAppend(outputPathTextDuration, str(tdItem.duration) + "\n")

		index = index + 1
		print ("tts complete %s/%s"%(index, totalLen))
	
		
def audioAndTextDuration_to_movie(title, audioFilePath, tdFilePath, outputPath):

	textLines = readFileTolines(tdFilePath)
	
	textAudioLines = []
	totalLines = len(textLines)
	
	# 读取字幕文件
	for i in range(totalLines - 1):
		if i % 3 == 0:
			item = TextAudioItem()
			item.text = textLines[i]
			item.audioStart = textLines[i + 1]
			item.audioDuration = textLines[i + 2]
			textAudioLines.append(item)

	# 生成视频文件
	generateVideoByTextAndAudio(outputPath, title, textAudioLines, audioFilePath)

def genMovieAndAudioByText(dirName, limitCount = 1, replace = False, inputRootDir = "data", outputRootDir = "output"):
	name = dirName
	fileRootPath = changeToAbsPath(os.path.join(inputRootDir, name))
	outputRootPath = changeToAbsPath(os.path.join(outputRootDir, name))
	ensure_dir(outputRootPath)
	print (fileRootPath)
	print (outputRootPath)

	filePathes = getAllFiles(fileRootPath)

	fileIndex = 0;
	totalLen = len(filePathes)
	for filePath in filePathes:
		fileName = os.path.basename(filePath)

		fileIndex = fileIndex + 1
		if limitCount != -1 and fileIndex > limitCount:
			break

		# 生成音频存放路径
		audioFilePath = os.path.join(outputRootPath, fileName)
		audioFilePath = audioFilePath + "." + AUDIO_FORMAT

		# 生成字幕存放路径, 是音频文件添加.td
		tdFilePath = audioFilePath + "." + TD_FORMAT

		# 生成 视频路径
		movieFilePath = os.path.join(outputRootPath, fileName)
		movieFilePath = movieFilePath + "." + MOVIE_FORMAT

		if replace:
			deleteFile(audioFilePath)
			deleteFile(tdFilePath)
			deleteFile(movieFilePath)

		# 如果存在了不需要处理
		if fileExist(audioFilePath) : 
			print ("local exist audio and td file pass")
		else:
			tts_to_file(filePath, audioFilePath, tdFilePath)
		
		# 如果存在了不需要处理
		if fileExist(movieFilePath) : 
			print ("local exist movie file pass")
		else:
			audioAndTextDuration_to_movie(fileName, audioFilePath, tdFilePath, movieFilePath)

		print ("complete %s/%s %s"%(fileIndex, totalLen, fileName))

if __name__ == "__main__":
	# genMovieAndAudioByText("我什么时候无敌了", 1, True, "data", "output")
	genMovieAndAudioByText("测试数据", -1, True, "test", "output")
		





