# -*- encoding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import codecs

import config

    

def parsing_date(url, file):
    response = requests.get(url, verify = False)
    if response.status_code == 200:
        srs = response.text
        soup = BeautifulSoup(srs, "html.parser")
        fout =  codecs.open(f'project/{file}', 'r', "utf-8")

        if fout.read() != str(soup.find(class_='last-update-date').string):
            fout =  codecs.open('project/last_update_date1.txt', 'w+', "utf-8")
            print('Не совпадают')              
            fout.seek(0)
            update_date_as_syte = soup.find(class_='last-update-date').string
            send_in_telegram(update_date_as_syte)
            fout.write(update_date_as_syte)
            fout.close()

        else:
            fout.close()
            print('Cовпадают')
    else:
        print(response.status_code)




def send_in_telegram(mesege_for_telegram):
    print(f'Запущен{mesege_for_telegram}')
    url = f'https://api.telegram.org/bot{config.token}/sendMessage'
    data = {'chat_id': config.channel_name, 'text': mesege_for_telegram}
    response = requests.post(url, data).json()
    print(response)


print('Первый url')
parsing_date(config.url_1, config.name_file_1)
print('Второй url')
parsing_date(config.url_2, config.name_file_2)