#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
import sys
import re
from utils import *


# 角色
SegmentRole_VoiceOver = "旁白"
SegmentRole_Person = "人物"

class Segment:
	endChar = "" #  Object 
	words = "" # <Objcet> []
	role = SegmentRole_VoiceOver

	def __str__(self):
		return self.endChar + "" + self.words


# split by \n
# end with 。/ ？ / !
def textToSegmentByLines(text):
	segments = [] 

	sep = "[\n]|[\:]|[\：]"
	wordsList = re.split(sep, text)
	
	totalLen = len(wordsList)
	for i in range(totalLen):
		words = getWordsFromList(wordsList, i)
		if len(words) > 0 :
			seg = Segment();
			seg.endChar = words[-1]
			seg.words = words;

			if isTalkWords(words):
				seg.role = SegmentRole_Person
			else:
				seg.role = SegmentRole_VoiceOver
			segments.append(seg)

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
	filePath = "./data/我什么时候无敌了/第1章 养的鸡竟是凤凰"
	str = readFile(filePath)

	segments = textToSegmentByLines(str)
	for seg in segments:
		print(seg.role + "--" + seg.words)






