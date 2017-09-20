from gtts import gTTS
from urllib import urlopen
import nltk
import os
from bs4 import BeautifulSoup

url = raw_input("Enter the news website url starting with 'https://' :- ")
html = urlopen(url).read() 
soup = BeautifulSoup(html)
[s.extract() for s in soup('script')]
x = soup.get_text()
y = "".join(x.split("\n"))
y = "".join(y.split("\r"))
y = "".join(y.split("-"))
y = "".join(y.split("."))
y = "".join(y.split(">"))
y = "".join(y.split("|"))
y = "".join(y.split("'"))
y = "".join(y.split("^"))
print(y)

myobj = gTTS(text=y, lang='en', slow=False)
myobj.save("sample1.mp3")
os.system("mpg321 sample1.mp3")
