#!/usr/bin/python
# -*- coding: UTF-8 -*-
from utils import *

def getAppleVoicenames():
    """I am returning the names of the voices available on Mac OS X."""
    voices = NSSpeechSynthesizer.availableVoices()
    voicenames = []
    for voice in voices:
        voiceattr = NSSpeechSynthesizer.attributesForVoice_(voice)
        voicename = voiceattr['VoiceName']
        if voicename not in voicenames:
            voicenames.append(voicename)
    return voicenames

def tts_apple(content, outputPath, voice = 'com.apple.speech.synthesis.voice.Mei-Jia', rate = 200, retryTimes = 0):
    from  AppKit import NSSpeechSynthesizer
    import sys  
    import Foundation

    LOGI("apple tts %s"%(content))

    try: 
        nssp = NSSpeechSynthesizer
        ve = nssp.alloc().init()
        ve.setRate_(rate)
        ve.setVoice_(voice)
        url = Foundation.NSURL.fileURLWithPath_(outputPath)
        ve.startSpeakingString_toURL_(content, url)
        del ve
        return True
    except:
        LOGE("apple tts retryTimes %s %s"%(str(retryTimes),content)) 
        retryTimes = retryTimes + 1;
        if retryTimes > 3:
            return False

        return tts_apple(content, outputPath, voice, rate, retryTimes)
    


def get_ness_default_voice():
	return 'com.apple.speech.synthesis.voice.Mei-Jia'
	