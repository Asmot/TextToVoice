#!/usr/bin/python
# -*- coding: UTF-8 -*-
 

import os
import sys
import shutil


def ensure_dir(file_path):

    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def readFile(filePath):
    f = open(filePath)
    lines = f.read()
    f.close()
    return lines

def writeFile(file_path,con):
    ensure_dir(file_path)
    file1 = open(file_path, "w")  
    file1.write(con)
    file1.close()  



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

def changeToAbsPath(path):
    if os.path.isabs(path):
        return path

    root_dir = os.path.abspath("")

    newPath =root_dir + "/" + path

    newPath = newPath.replace("./","/")
    newPath = newPath.replace("//","/")
    return newPath


    
