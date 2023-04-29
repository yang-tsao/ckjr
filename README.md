# ckjr
创客匠人视频下载
本项目依赖于yt-dlp、requests等项目。可以下载ckjr的视频。注意代码中的Bearer需手动换成自己的。

Bearer可以通过以下方式取得
1. 打开创客匠人的具体视频页面，如果是Chrome系的浏览器按F12打开开发者工具，其他浏览器请自行查询。
2. 切换到console（“终端”）页面，输入以下代码：
```javascript
"Bearer " + localStorage.getItem("token")
```
3. 将输出的结果粘贴到all_dl.py与course_dl.py中即可。

注：未经完整测试，如果不能使用，请用户自行修改代码。如果需要调用dirs API才能获取视频网址，可以考虑使用decrypt.py提供的解密函数解密视频的url('videoUrlEncode'与'videoMp4UrlEncode')。
