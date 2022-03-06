
# 任务
## 小说文本下载
	奇书网 http://www.qishu.me/
	爬取数据 

## 内容识别
### 识别语句
	小说内容读取，按换行拆分成一句话


## 一句话转换为音频
### 百度TTS 
	去百度开放平台申请key，按照例子调用即可
	缺点：网络调用，需要收费

### nsss
	mac 自带TTS，可以把文字语音
	支持python直接调用

	优点：离线，没有调用限制
	缺点：只有一种声音，机器声音重


## 一句话转换成视频背景，并将音频和视频合并
	moviepy
### 遇到的问题
#### 找不到 ImageMagick
~~~
	brew install imagemagick@6
~~~

	安装完成后设置环境变量
~~~
	export IMAGEMAGICK_HOME="/usr/local/opt/imagemagick@6"
	export PATH="$IMAGEMAGICK_HOME/bin:$PATH"
~~~

#### 找不到ffmpeg
	brew install ffmpeg

	按照完成后执行拷贝
	cp -R ~/Downloads/ffmpeg-osx-v3.2.4 ~/Library/Application\ Support/imageio/ffmpeg/
	
#### 中文不行只能显示英文
	设置字体路径就可以了
	txt_clip = TextClip("this is 测试 test ",fontsize=70, color='red',font="./font/trends.ttf")

	字体下载 https://www.aigei.com/font/class/imitation_song/

