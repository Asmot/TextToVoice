#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

def tts_apple(content, outputPath, voice = 'com.apple.speech.synthesis.voice.Mei-Jia', rate = 200):
    from  AppKit import NSSpeechSynthesizer
    import sys  
    import Foundation

    print("apple tts %s"%(content))

    nssp = NSSpeechSynthesizer
    ve = nssp.alloc().init()
    ve.setRate_(rate)
    ve.setVoice_(voice)
    url = Foundation.NSURL.fileURLWithPath_(outputPath)
    ve.startSpeakingString_toURL_(content, url)


def get_ness_default_voice():
	return 'com.apple.speech.synthesis.voice.Mei-Jia'
	