import requests,csv
from bs4 import BeautifulSoup

with open('drugnews2.csv','w') as csvfile:
    writer = csv.writer(csvfile)

    links_2 = ['http://www.bharian.com.my/search?s=jenayah%20dadah&page=23','http://www.bharian.com.my/search?s=jenayah%20dadah&page=24','http://www.bharian.com.my/search?s=jenayah%20dadah&page=25','http://www.bharian.com.my/search?s=jenayah%20dadah&page=26','http://www.bharian.com.my/search?s=jenayah%20dadah&page=27','http://www.bharian.com.my/search?s=jenayah%20dadah&page=28','http://www.bharian.com.my/search?s=jenayah%20dadah&page=29','http://www.bharian.com.my/search?s=jenayah%20dadah&page=30','http://www.bharian.com.my/search?s=jenayah%20dadah&page=31','http://www.bharian.com.my/search?s=jenayah%20dadah&page=32','http://www.bharian.com.my/search?s=jenayah%20dadah&page=33','http://www.bharian.com.my/search?s=jenayah%20dadah&page=34','http://www.bharian.com.my/search?s=jenayah%20dadah&page=35','http://www.bharian.com.my/search?s=jenayah%20dadah&page=36','http://www.bharian.com.my/search?s=jenayah%20dadah&page=37','http://www.bharian.com.my/search?s=jenayah%20dadah&page=38','http://www.bharian.com.my/search?s=jenayah%20dadah&page=39']

    for url in links_2:
        page = requests.get(url)
        #print(page.text)
        page_data = BeautifulSoup(page.text)
        news = page_data.find_all('div',class_='view-content')

        for items in news:
            title = items.find('h2',class_='news-title')
            date = items.find('div',class_='date-search')
            lead = items.find('p',class_='lead')
            # print(title.text)
            # print(title.text,'\n',date.text,'\n',lead.text)
            news_list2 = [title.text,date.text,lead.text]
            writer.writerow(news_list2)
