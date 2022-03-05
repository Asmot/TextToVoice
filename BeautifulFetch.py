#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests  
from bs4 import BeautifulSoup
import re
from utils import *

class Chapter :
	name = ""
	url = ""
	content = ""


def fetch_bqkan_content(url):
	print(url)
	strHtml = requests.get(url) 
	html = strHtml.text
	bf = BeautifulSoup(html,"html.parser")

	texts = bf.find_all(class_ = "txt")
	result = ""
	# print (len(texts))
	for item in texts:	
		result = result + item.text.decode('utf8')
		# print (result)
	return result


def fetch_bqkan_all_chapter(baseurl, id):
	strHtml = requests.get(baseurl + id) 
	html = strHtml.text
	bf = BeautifulSoup(html,"html.parser")

	# menu_ul = bf.find_all('ul',class_ = "cf")
	# hrefs = menu_ul.find_all('a')
	hrefs = bf.find_all('a')
	
	result = []
	for href in hrefs:
		itemHref = href.get("href")
		itemName = href.text.decode('utf8')

		if len(itemName) == 0 :
			continue

		if "开始阅读" in itemName :
			continue
		if "更新至 " in itemName :
			continue

		# check valid href
		if id in itemHref:
			item = Chapter()
			item.url = baseurl + itemHref
			item.url = item.url.replace(baseurl +"/",baseurl)
			item.name = itemName
			result.append(item)
			# print(item.url)
			
	return result
	

if __name__ == "__main__":
	bookName = "我什么时候无敌了"
	mainBaseUrl = "https://www.qu-la.com/"
	bookId = "booktxt/69239612116"
	url = "https://www.qu-la.com/booktxt/69239612116/13191720116.html"

	rootPath = "./data/" + bookName
	rootPath = changeToAbsPath(rootPath)
	# ensure rootPath
	ensure_dir(rootPath)

	chapters = fetch_bqkan_all_chapter(mainBaseUrl, bookId)

	total = len(chapters)

	count = 0;
	for chapter in chapters:
		print ("%s/%s"%(count,total) + ":" + chapter.name)
		count = count +1;
		file_path = rootPath + "/" + chapter.name
		if fileExist(file_path) : 
			print ("local exist pass")
			continue

		chapter.content = fetch_bqkan_content(chapter.url)

		chapter.content = chapter.content.replace("『如果章节错误，点此举报』","")
		writeFile(file_path, chapter.content)

		
		# if count > 10:
		# 	break
