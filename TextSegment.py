#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
import sys
import re

class Segment:
	endChar = "" #  Object 
	words = "" # <Objcet> []

	def __str__(self):
		return self.endChar + "" + self.words

# split by \n
# end with 。/ ？ / !
def textToSegment(text):
	segments = [] 
	res = re.split("(?<=[。!?\n])\s+", text)
	for element in res:

		seg = Segment();
		seg.endChar = element[-1]
		seg.words = element;

		segments.append(seg)

	print (segments[3].endChar)
	print (segments[3].words)


# split by \n
# end with 。/ ？ / !
def textToSegmentByLines(text):
	segments = [] 
	res = re.split("(?<=[\n])\s+", text)
	for element in res:

		seg = Segment();
		seg.endChar = element[-1]
		seg.words = element;

		segments.append(seg)
	return segments

