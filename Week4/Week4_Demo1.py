import urllib.request
import os
from bs4 import BeautifulSoup

os.chdir('C:/Users/KY/Google Drive/CUHKPyTutorial2019/Week4')

url = 'https://emojiisland.com/pages/free-download-emoji-icons-png'
req = urllib.request.urlopen(url)
html = req.read()
print(len(html))

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags

tags = soup('img')
os.makedirs('png', exist_ok=True)

for tag in tags:
  
    imgurl = tag.get('src')
    if (not ('png' in imgurl)):
        continue
    try:
        outimgname = os.path.basename(imgurl).split('?')[0]
        if ('http' in imgurl):
            urllib.request.urlretrieve(imgurl, os.path.join('png', outimgname))
        else:
            urllib.request.urlretrieve('https:' + imgurl, os.path.join('png', outimgname))
    except:
        print(outimgname + ' Get Error.')    
        continue     


# In addition
# Request Status
print(req.status)
# Get the title of webpage: web_title
print(soup.title)
# Prettify the BeautifulSoup object: pretty_soup
print(soup.prettify())
# Get web text: web_text
print(soup.get_text())
# Find all 'a' tags (which define hyperlinks): a_tags
print(soup.find_all('a'))
# tag list: https://www.w3schools.com/tags/ref_byfunc.asp