### BrightTalk downloader (btdl)

Download videos from BrightTalk with a GUI interface

<img src='/Images/GUI.JPG'>

### Instructions

1. Download or `git clone git@github.com:alfredzou/BrightTalk-video-downloader.git`
2. Download [ffmpeg](https://www.ffmpeg.org/download.html)
3. Edit the environment path to include ffmpeg.exe folder
4. Login to BrightTalk
5. Navigate to video page and obtain the URL of the .m3u8 file
    1. Open chrome
    2. Open the developer tools in the top left or (cntrl + shift + i)
    3. Open the networks tab
    4. Filter by .m3u8 
    5. Right click .m3u8 URL and copy URL

<img src='/Images/URL example.gif'>

6. Open the downloaded folder
7. `python btdl.py`
8. Input .m3u8 URL, file name and download folder, and download!

<img src='/Images/GUI.JPG'>