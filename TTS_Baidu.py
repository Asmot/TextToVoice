#!/usr/bin/python
# -*- coding: UTF-8 -*-

APP_ID = '25709228'
API_KEY = 'oOUMpGrZzj71M6F4MlZavOD2'
SECRET_KEY = 'xprrvxGX5VmthpIbZMtRfQAjxUxQ0EBC'

def tts_baidu(content, outputPath):
	import subprocess
	import shlex
	from aip import AipSpeech

	print("baidu tts %s"%(content))

	aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
	result = aipSpeech.synthesis(content, 'zh', 1, {'vol': 5,'per':4})
	if not isinstance(result, dict):
	    with open(outputPath, 'ab+') as f:
	        f.write(result)
