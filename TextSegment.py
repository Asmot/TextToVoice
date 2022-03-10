#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
import sys
import re
from utils import *
from role import *

class Segment:
	endChar = "" #  Object 
	words = "" # <Objcet> []
	role = SegmentRole_VoiceOver

	def __str__(self):
		return self.endChar + "" + self.words

def isValid(words):
	if len(words) == 0:
		return False
	if "ｈｔｔｐ" in words:
		return False
	if "\/\/" in words:
		return False
	if "//" in words:
		return False
	if "记住网址" in words:	
		return False
	if "\“" == words:	
		return False
	if "“" == words:	
		return False
	if words == '[]':
		return False
	if words == '()':
		return False
	if words == '”':
		return False
	return True

# split by \n
# end with 。/ ？ / !
def textToSegmentByLines(text):
	segments = [] 

	sep = "[\n]|[\:]|[\：]"
	wordsList = re.split(sep, text)
	
	totalLen = len(wordsList)
	for i in range(totalLen):
		words = getWordsFromList(wordsList, i)
		if isValid(words):
			seg = Segment();
			seg.endChar = words[-1]
			seg.words = words;

			if isTalkWords(words):
				seg.role = SegmentRole_Person
			else:
				seg.role = SegmentRole_VoiceOver
			segments.append(seg)
		else:
			LOGE ("invalid words %s"%(str(words)))

	return segments

# 是否是说出来的话
# 引号和中括号包含的就是 说出来的话, 需要匹配开头，用match匹配
# 中间带引号的不算
def isTalkWords(words):
	if re.match('\".*\"', words):
		return True

	if re.match('\“.*\”', words):
		return True

	if re.match('\【.*\】', words):
		return True
	return False
	

def getWordsFromList(wordsList, index):
	if index >= 0 and index < len(wordsList):
		return wordsList[index].strip()
	else:
		return None


if __name__ == "__main__":
	filePath = "./data/我什么时候无敌了1062/第1087章 应该是个狂妄且有些小聪明的人"
	str = readFile(filePath)

	segments = textToSegmentByLines(str)
	print(segments[0].role + "--" + segments[0].words)
	# for seg in segments:
	# 	print(seg.role + "--" + seg.words)






