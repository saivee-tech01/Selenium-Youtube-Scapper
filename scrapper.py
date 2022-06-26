import requests
YOUTUBE_TRENDING_URL="https://www.youtube.com/feed/trending"
response=requests.get(YOUTUBE_TRENDING_URL)
print('STATUS CODE',response.status_code)
#print('OUTPUT',response.text[:500])
with open('trending.html','w') as f:
  f.write(response.text)