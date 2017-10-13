from __future__ import unicode_literals

import urllib
import urllib2
import sys
import os


from bs4 import BeautifulSoup

import youtube_dl

if len(sys.argv) != 2:
	print "Using python download_yotube.py <video_name>"
	sys.exit()


print sys.argv[1]
textToSearch = sys.argv[1]


query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,"html.parser")
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	if "googleads" not in vid['href'] and "list" not in vid['href']:
		first_link = 'https://www.youtube.com' + vid['href']
		break

print first_link


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([first_link])