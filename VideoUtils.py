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

# def get

# 文本和字幕的播放时长和播放开始位置
class TextAudioItem:
	text = ""
	audioDuration = 0
	audioStart = 0

def generateVideoByTextAndAudio(file_path, title, textAudioLines, audio_path):
	screensize = (720,460)
	titlePos = ("center",10)
	textPos = ("center","center")
	# videoFile = VideoFileClip(file_path);
	audio_clip = AudioFileClip(audio_path)
	duration = audio_clip.duration;
	print (audio_clip.duration)

	text_clips = []
	title_clip = TextClip(title,fontsize=70, color='red',font="./font/trends.ttf")
	title_clip = title_clip.set_pos(titlePos)
	title_clip = title_clip.set_duration(duration)
	title_clip = title_clip.set_audio(audio_clip);
	text_clips.append(title_clip)

	index = 0;

	totalTextDuration = 0
	for item in textAudioLines:		
		curDuration = float(item.audioDuration)
		curStart = item.audioStart;
		print ("start %s/%s duration %s text: %s" %(str(curStart), str(duration), str(item.audioDuration), item.text))
		# 记录总时长，作为下一个字幕的起点
		totalTextDuration = totalTextDuration + curDuration;

		line_clip = TextClip(item.text, fontsize=40, color='yellow',font="./font/trends.ttf")
		line_clip = line_clip.set_pos(textPos)
		line_clip = line_clip.set_start(curStart)
		line_clip = line_clip.set_duration(curDuration)

		index = index + 1
		text_clips.append(line_clip)

	# 合并
	videoFile = CompositeVideoClip(text_clips, size=screensize)
	videoFile = videoFile.set_duration(duration)

	videoFile.write_videofile(file_path, fps=15)


# if __name__ == "__main__":	
# 	title = "第1章 养的鸡竟是凤凰"
# 	text_file_path = changeToAbsPath("./output/我什么时候无敌了/第1章 养的鸡竟是凤凰.wav.td")
# 	file_path = changeToAbsPath("./output/001.mp4")
# 	audio_path = changeToAbsPath("./output/我什么时候无敌了/第1章 养的鸡竟是凤凰.wav")
# 	textLines = readFileTolines(text_file_path)
	
# 	textAudioLines = []
# 	totalLines = len(textLines)
# 	print (totalLines)
# 	for i in range(totalLines - 1):
# 		if i % 2 == 0:
# 			item = TextItem()
# 			item.text = textLines[i]
# 			item.audioDuration = textLines[i + 1]
# 			textAudioLines.append(item)

# 	generateVideoByTextAndAudio(file_path, title, textAudioLines, audio_path)
# 	# generateVideoByText(file_path, text)

