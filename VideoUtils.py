#!/usr/bin/python
# -*- coding: UTF-8 -*-
# python 2.x

# Import everything needed to edit video clips
from moviepy.editor import *
from utils import *


def generateVideoByText(file_path, text):
	# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
	# clip = VideoFileClip(file_path).subclip(50,60)

	# # Reduce the audio volume (volume x 0.8)
	# clip = clip.volumex(0.8)

	# Generate a text clip. You can customize the font, color, etc.
	txt_clip = TextClip("this is 测试 test ",fontsize=70, color='red',font="./font/trends.ttf")

	# Say that you want it to appear 10s at the center of the screen
	txt_clip = txt_clip.set_pos('center').set_duration(10)

	# Overlay the text clip on the first video clip
	# video = CompositeVideoClip([txt_clip])
	# video = VideoClip(make_frame, duration=2)

	# Write the result to a file (many options available !)
	txt_clip.write_videofile(file_path, fps=15)

if __name__ == "__main__":	
	text = "我什么时候无敌了"
	file_path = changeToAbsPath("./output/001.mp4")
	generateVideoByText(file_path, text)

