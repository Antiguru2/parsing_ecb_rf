# -*- encoding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import codecs

import config

    

def parsing_date(url, file_name):
    response = requests.get(url, verify = False)
    if response.status_code == 200:
        srs = response.text
        soup = BeautifulSoup(srs, "html.parser")
        file =  codecs.open(f'project/{file_name}', 'r', "utf-8")

        if file.read() != str(soup.find(class_='last-update-date').string):
            file =  codecs.open(f'project/{file_name}', 'w+', "utf-8")
            print('Не совпадают')              
            update_date_as_syte = soup.find(class_='last-update-date').string
            send_to_telegram(update_date_as_syte)
            file.write(update_date_as_syte)
            file.close()

        else:
            file.close()
            print('Cовпадают')
    else:
        print(response.status_code)




def send_to_telegram(mesege_for_telegram):
    print(f'Запущен{mesege_for_telegram}')
    url = f'https://api.telegram.org/bot{config.token}/sendMessage'
    data = {'chat_id': config.channel_name, 'text': mesege_for_telegram}
    response = requests.post(url, data).json()
    print(response)


print('Первый url')
parsing_date(config.url_1, config.name_file_1)
print('Второй url')
parsing_date(config.url_2, config.name_file_2)