import requests
from lxml import html


page = requests.get('https://azure.microsoft.com/en-us/support/faq/')
data = html.fromstring(page.content)

for entry in data.xpath('//li[@class="faq-entry"]'):
    question = entry.xpath('button/text()')[0]
    answer = entry.xpath('div/p/text()')
