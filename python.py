import pandas as pd
import requests, bs4, os, codecs, csv
from bs4 import BeautifulSoup
# import os
# import sys
from csv import DictReader


# Below we need to provide a csv ource file where all of the urls reside
with open('weathertest13.csv') as f:
    r = csv.reader(f)

    for row in r:
        page = requests.get(row[0])
        print('step1')
        print(page.status_code)
        print('step2')
        print(page.content)
        soup = BeautifulSoup(page.content, 'html.parser')
        print('step3')
        print(soup.prettify())
        print('step4')
        print(list(soup.children))
        print('step5')
        print([type(item) for item in list(soup.children)])
        #body = soup.find('tbody')
        #values = soup.find('td')
        print('step6')
        print(soup.findAll('tbody',limit=2)[0].findAll('td'))  #trying to change tbody
        #print('step6.5')
        #print(soup.findAll('table'))
        print('step7')
        column_headers = [th.getText() for th in
                          soup.findAll('tr', limit=None)[33].findAll('th')]
        print(column_headers)

        print('step8')
        data_rows = soup.findAll('tr')[34:]

        print(type(data_rows))

        weather_obs = [[td.getText() for td in data_rows[i].findAll(['td', 'th'])]
                       for i in range(len(data_rows))]
        print('step9')
        print(weather_obs)

        print('step10')
        df = pd.DataFrame(weather_obs, columns=column_headers)
        # df.assign(C = 'Page')
        df['weather_link'] = (row[0])
        print(df)  # head() lets us see the 1st 5 rows of our DataFrame by default
        print('step11 - writes df to csv file')
        df.to_csv('C:\Python\demo4.csv',encoding='utf-8')

        #import os

        # if file does not exist write header
        # This is where we need to identify an output file for the data (note: change the file name 3 times below)
        #if not os.path.isfile('soupworksdemow2.csv'):
          #  df.to_csv('soupworksdemow2.csv', header='column_names')
       # else:  # else it exists so append without writing the header
         #   df.to_csv('soupworksdemow2.csv',encoding='utf-8-sig')