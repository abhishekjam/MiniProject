from newspaper import Article
def mainmodule1(url):
    article = Article(url, language="en")
    article.download()
    article.parse()
    article.nlp()
    return article.title
def mainmodule2(url):
    article = Article(url, language="en")
    article.download()
    article.parse()
    article.nlp()
    return article.authors
def mainmodule3(url):
    article = Article(url, language="en")
    article.download()
    article.parse()
    article.nlp()
    return article.text
url1 = raw_input("Enter the news website url starting with 'https://' :- ")
result1 = mainmodule1(url1)
print(result1)
print("\n")
result2 = mainmodule2(url1)
print(result2)
print("\n")
result3 = mainmodule3(url1)
print(result3)