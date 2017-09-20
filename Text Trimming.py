from urllib import urlopen
import nltk
from bs4 import BeautifulSoup

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
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
