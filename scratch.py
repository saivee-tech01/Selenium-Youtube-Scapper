import requests
from bs4 import BeautifulSoup
YOUTUBE_TRENDING_URL="https://www.youtube.com/feed/trending"
response=requests.get(YOUTUBE_TRENDING_URL)
print('STATUS CODE',response.status_code)
#print('OUTPUT',response.text[:500])
with open('trending.html','w') as f:
  f.write(response.text)

doc=BeautifulSoup(response.text,'html.parser')
print('PageTitle',doc.title.text)

#Find all video divs
video_div=doc.find_all('div',class_='ytd-video-renderer')
print(f'Found {len(video_div)} videos')