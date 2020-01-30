import requests
import bs4
import webbrowser

def openurl(url):
    webbrowser.get('firefox').open_new_tab(url)


link = input('enter flickr link: ')

a = link

res = requests.get(a)

c = res.text

soup = bs4.BeautifulSoup(res.text, 'html.parser')


html = soup

txt2 = html.get_text().split('"')

result = [i for i in txt2 if i.startswith('\\/\\/')]

newlist = [word for word in result if word.endswith('h.jpg')]

replaceword = [s.replace('\\/\\/', 'https://') for s in newlist]

replaceword1 = [s.replace('\\', '') for s in replaceword]

duplicate = replaceword1
noduplicate = list(dict.fromkeys(duplicate))
print(noduplicate)

numbertoshow = 5

shownumber = noduplicate[:numbertoshow]

print(len(shownumber))

print(len(newlist))

for everylink in shownumber:
  openurl(everylink)

