#!/usr/bin/python
# -*- coding: UTF-8 -*-

APP_ID = '25709228'
API_KEY = 'oOUMpGrZzj71M6F4MlZavOD2'
SECRET_KEY = 'xprrvxGX5VmthpIbZMtRfQAjxUxQ0EBC'

BAIDU_VOICE_DEFAULT = 0
BAIDU_VOICE_MALE_XIAOYAO = 5003
BAIDU_VOICE_MALE_BOWEN = 106

def tts_baidu(content, outputPath, voicePer = BAIDU_VOICE_DEFAULT):
	import subprocess
	import shlex
	from aip import AipSpeech

	print("baidu tts %s"%(content))

	aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
	result = aipSpeech.synthesis(content, 'zh', 1, {'vol': 5,'per':voicePer })
	if not isinstance(result, dict):
	    with open(outputPath, 'ab+') as f:
	        f.write(result)
