#!/usr/bin/python
# -*- coding: UTF-8 -*-

from utils import *

from TextSegment import *
from TTSUtil import *
from VideoUtils import *
import traceback

AUDIO_FORMAT = "wav"
TD_FORMAT = "td"
MOVIE_FORMAT = "mp4"

def getAllFiles(dir):
	fileNames = listFiles(dir)
	total_len = len(fileNames)

	result = []
	fileNames.sort()
	for name in fileNames:
		result.append(name)
	return result

## 生成语音和字幕文件
## 字幕文件以td结尾 内容是 文本和时长，换行分割
def tts_to_file(filePath, outputPath, outputTdPath):
	outputPathTextDuration = outputTdPath
	LOGE (filePath + " ================> " + outputPath)
	fileCon = readFile(filePath)
	## text to words segments

	index = 0;
	segments = textToSegmentByLines(fileCon)
	totalLen = len(segments)
	for seg in segments:
		# 如果words有标点符号会被拆分为多个
		tdItems = tts_role(seg.words, outputPath, AUDIO_FORMAT, seg.role);
		if TTS_FLAG_FAILED == tdItems:
			deleteFile(outputPath)
			deleteFile(outputTdPath)
			LOGE("tts_role failed %s"%(seg.words))
			return
		for tdItem in tdItems:
			LOGI ("保存字幕: %.2f, %.2f text %s"%(tdItem.start, tdItem.duration, tdItem.text))

			# 保存文本和文本播放时长，用来制作字幕
			writeFileAppend(outputPathTextDuration, tdItem.text)
			if not tdItem.text.endswith("\n"):
				# 保证换行
				writeFileAppend(outputPathTextDuration, "\n")
				
			writeFileAppend(outputPathTextDuration, str(tdItem.start) + "\n")
			writeFileAppend(outputPathTextDuration, str(tdItem.duration) + "\n")

		index = index + 1
		if len(tdItems) > 0:
			print ("------ tts complete %s/%s %s..."%(index, totalLen,seg.words[0:5]))
		else:
			print ("------ tts pass     %s/%s %s..."%(index, totalLen,seg.words[0:5]))
	
		
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
	LOGE (fileRootPath)
	LOGE (outputRootPath)

	
	filePathes = getAllFiles(fileRootPath)

	fileIndex = 0;
	totalLen = len(filePathes)
	for filePath in filePathes:
		fileName = os.path.basename(filePath)
		
		# 生成音频存放路径
		audioFilePath = os.path.join(outputRootPath, fileName)
		audioFilePath = audioFilePath + "." + AUDIO_FORMAT

		# 生成字幕存放路径, 是音频文件添加.td
		tdFilePath = audioFilePath + "." + TD_FORMAT

		# 生成 视频路径
		movieFilePath = os.path.join(outputRootPath, fileName)
		movieFilePath = movieFilePath + "." + MOVIE_FORMAT
		try:
			if replace:
				deleteFile(audioFilePath)
				deleteFile(tdFilePath)
				deleteFile(movieFilePath)

			# 如果存在了不需要处理
			if fileExist(audioFilePath) : 
				LOGE ("local exist audio and td file pass %s"%(audioFilePath[0:5]))
			else:
				tts_to_file(filePath, audioFilePath, tdFilePath)
			
			# 如果存在了不需要处理
			if fileExist(movieFilePath) : 
				LOGE ("local exist movie file pass %s"%(movieFilePath[0:5]))
				continue
			else:
				audioAndTextDuration_to_movie(fileName, audioFilePath, tdFilePath, movieFilePath)

			LOGE ("complete %s/%s %s"%(fileIndex, totalLen, fileName))

			fileIndex = fileIndex + 1
			if limitCount != -1 and fileIndex > limitCount:
				break
		except Exception as e:
			
			LOGE("genMovieAndAudioByText exception, delete file")

			deleteFile(audioFilePath)
			deleteFile(tdFilePath)	
			deleteFile(movieFilePath)

			LOGE(e)
			traceback.print_exc()
			return False

if __name__ == "__main__":
	# genMovieAndAudioByText("我什么时候无敌了", 1, True, "data", "output")
	genMovieAndAudioByText("我什么时候无敌了1062", 1, False, "data", "output")
	# genMovieAndAudioByText("测试数据", -1, True, "test", "output")
		





