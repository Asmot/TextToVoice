#!/usr/bin/python
# -*- coding: UTF-8 -*-

from utils import *

from TextSegment import *
from AipSpeechUtil import *


if __name__ == "__main__":
	filePath = "./data/我想只想躺赢-1"
	outputPath = "./output/我想只想躺赢-1.wav"

	filePath = changeToAbsPath(filePath)
	outputPath = changeToAbsPath(outputPath)

	fileCon = readFile(filePath)

	## text to words segments
	segments = textToSegmentByLines(fileCon)

	index = 0;
	totalLen = len(segments)
	for seg in segments:
		textToWav(seg.words, outputPath);
		print ("complete %s/%s"%(index, totalLen))
		index = index + 1
		if index > 5:
			break



