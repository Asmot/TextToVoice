# -*- coding:utf-8 -*-
import subprocess
import shlex
from aip import AipSpeech


APP_ID = '25709228'
API_KEY = 'oOUMpGrZzj71M6F4MlZavOD2'
SECRET_KEY = 'xprrvxGX5VmthpIbZMtRfQAjxUxQ0EBC'

def textToWav(content, outputPath):
	aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
	print ("\ttextToWav %s..."%(content[0:10]))
	result = aipSpeech.synthesis(content, 'zh', 1, {'vol': 5,'per':4})
	if not isinstance(result, dict):
	    with open(outputPath, 'ab+') as f:
	        f.write(result)
