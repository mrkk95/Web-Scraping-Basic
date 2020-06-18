import requests
from bs4 import BeautifulSoup
url = "https://mrkk95.github.io/portfolio_keyur_khunadiya/"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup)
#print(soup.prettify)

title = soup.title
#print(title)
#print(type(title))
#print(type(title.string))

paras1 = soup.find_all('div')
#print(paras1)

paras2 = soup.find_all('meta')
#print(paras2)

markup = "<p><!--this is comment from mr.kk--></p>"
soup2 = BeautifulSoup(markup)
#print(soup2.p.string)
#print(type(soup2.p.string))

#print(soup.find('div')['class'])

#print(soup.find_all("div",class_="row"))

#print(soup.find('div').get_text())

#print(soup.get_text())

ele = soup.select('#a')
#print(ele)

links = soup.find_all('link')
#print(links)
all_link = set()

for link in links:
    if(link.get('href') != '#'):
        all_link.add(link.get('href'))
#print(all_link)

contacts = soup.find(id='contact')
#print(contacts.childern)
#print(contacts.content)
#print(contacts.parent)