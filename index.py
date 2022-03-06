#!/usr/bin/python
# -*- coding: UTF-8 -*-

from utils import *

from TextSegment import *
from AipSpeechUtil import *

AUDIO_FORMAT = "wav"

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

def tts_to_file(filePath, outputPath):
	print (filePath + " => " + outputPath)
	fileCon = readFile(filePath)
	## text to words segments

	index = 0;
	segments = textToSegmentByLines(fileCon)
	totalLen = len(segments)
	for seg in segments:
		print (seg.words)
		tts_nsss(seg.words, outputPath, AUDIO_FORMAT);

		print ("tts complete %s/%s"%(index, totalLen))
		index = index + 1
		# if index > 10:
		# 	break

if __name__ == "__main__":
	fileRootPath = changeToAbsPath("./data/我什么时候无敌了")
	outputRootPath = changeToAbsPath("./output/我什么时候无敌了")
	ensure_dir(outputRootPath)

	filePathes = getAllFiles(fileRootPath)

	fileIndex = 0;
	totalLen = len(filePathes)
	for filePath in filePathes:
		fileName = os.path.basename(filePath)

		fileIndex = fileIndex + 1
		if fileIndex > 1:
			break
		print ("complete %s/%s %s"%(fileIndex, totalLen, fileName))
		outputPath = os.path.join(outputRootPath, fileName)
		outputPath = outputPath + "." + AUDIO_FORMAT

		if fileExist(outputPath) : 
			print ("local exist pass")
			continue
		tts_to_file(filePath, outputPath)
		

		

	# filePath = changeToAbsPath(filePath)
	# outputPath = changeToAbsPath(outputPath)

	# fileCon = readFile(filePath)

	# ## text to words segments
	# segments = textToSegmentByLines(fileCon)

	# index = 0;
	# totalLen = len(segments)
	# for seg in segments:
	# 	tts_nsss(seg.words, outputPath);
	# 	print ("complete %s/%s"%(index, totalLen))
	# 	index = index + 1
	# 	if index > 1:
	# 		break



