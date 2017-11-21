import requests
from lxml import html


page = requests.get('https://azure.microsoft.com/en-us/support/faq/')
data = html.fromstring(page.content)

counter = 0
for entry in data.xpath('//li[@class="faq-entry"]'):
    question = entry.xpath('button/text()')[0]
    answer = entry.xpath('div/p/text()')
    counter += 1
    with open(r'C:\Users\Taylor\Documents\Webscapper\Docs\qa{}.txt'.format(counter),'w') as f:
        f.write("".join([question, '\n', " ".join(answer)]))
        f.close
