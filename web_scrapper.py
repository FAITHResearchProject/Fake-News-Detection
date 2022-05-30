from requests_html import HTMLSession
session = HTMLSession()

url = 'INSERT URL HERE'

r = session.get(url)
r.html.render()
articles = r.html.find('article')

newslist = []

for item in articles:
    try:
        newsitem = item.find('h1', first=True)
        newsarticle = newsitem.text
        newslist.append(newsarticle)
    except:
        pass

print(newslist[0])