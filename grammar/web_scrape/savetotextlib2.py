from lxml import html
import requests
headers= {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}
page = requests.get('https://www.google.com/search?q=president+of+bangladesh', headers=headers)
tree = html.fromstring(page.content)
print(page.text)
hotel_name = tree.xpath('//span[@class="_XWK"]/text()')

print(hotel_name)


