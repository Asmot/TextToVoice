#!/usr/bin/python
# -*- coding: UTF-8 -*-
 

import os
import sys
import shutil
import re

DEBUG_LOG = False

def LOGE(text):
    print (text)

def LOGI(text):
    if DEBUG_LOG:
        print (text)


def ensure_dir(file_path):
    if not os.path.exists(file_path):
        LOGI ( "mkdir => " + file_path)
        os.makedirs(file_path)

def readFile(filePath):
    f = open(filePath)
    lines = f.read()
    f.close()
    return lines

def readFileTolines(filePath):
    f = open(filePath)
    lines = f.read()
    f.close()
    res = []
    temp = re.split("\n", lines)
    for item in temp:
        res.append(item)
    return res;


def writeFile(file_path,con):
    file1 = open(file_path, "w")  
    file1.write(con)
    file1.close()  

def writeFileAppend(file_path,con):
    file1 = open(file_path, "a")  
    file1.write(con)
    file1.close()  


def fileExist(file_path):
    if os.path.exists(file_path):
        return os.path.isfile(file_path)
    return False

def deleteFile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

#生成目录
def mkdir(path):

    path=path.strip()
    path=path.rstrip("\\")
    
    isExists=os.path.exists(path)
    if not isExists:

        os.makedirs(path) 
        return True
    else:
        return False

def findFiles(dir,filterEx):
    matches = []
    if os.path.isfile(dir):
        if filterEx in dir:
            matches.append(dir)
    else:
        for root,dirnames,filenames in os.walk(dir):
            for filename in filenames:
                if filterEx in filename:
                    matches.append(os.path.join(root,filename))
    return matches

def listFiles(dir):
    matches = []
    for root,dirnames,filenames in os.walk(dir):
        for filename in filenames:
            matches.append(os.path.join(root,filename))
    return matches


def splitStr(text, maxLen):
    textLen = len(text)
    textList = []
    maxLen = 20
    if textLen > maxLen:
        while True:
            cutA = text[: maxLen]
            cutB = text[maxLen: ]
            textList.append(cutA)
            if len(cutB) > maxLen:
                text = cutB
            else:
                textList.append(cutB)
                break
    else:
        textList.append(text)
    return textList

def splitWords(words):
    return re.split("[?\”\，\。]", words)

def changeToAbsPath(path):
    if os.path.isabs(path):
        return path

    root_dir = os.path.abspath("")

    newPath =root_dir + "/" + path

    newPath = newPath.replace("./","/")
    newPath = newPath.replace("//","/")
    return newPath


    
