# -*- encoding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import codecs

import config

    

def parsing_date():
    response1 = requests.get(f"https://екатеринбург.рф/%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D1%8F%D0%BC/%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/%D0%BF%D0%BB%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5%D0%9E%D0%9E/%D0%A2%D0%A4", verify = False)
    response2 = requests.get(f"https://екатеринбург.рф/%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D1%8F%D0%BC/%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/%D0%BF%D0%BB%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5%D0%9E%D0%9E/%D1%81%D1%80%D0%BE%D1%87%D0%BD%D0%BE", verify = False)
    if response1.status_code == 200 and response2.status_code == 200:
        srs1 = response1.text
        srs2 = response2.text
        soup1 = BeautifulSoup(srs1, "html.parser")
        soup2 = BeautifulSoup(srs2, "html.parser")
        fout1 =  codecs.open('project/last_update_date1.txt', 'r', "utf-8")
        fout2 =  codecs.open('project/last_update_date2.txt', 'r', "utf-8")

        if fout1.read() != str(soup1.find(class_='last-update-date').string) or fout2.read() != str(soup2.find(class_='last-update-date').string) :
            fout1 =  codecs.open('project/last_update_date1.txt', 'r', "utf-8")
            fout2 =  codecs.open('project/last_update_date2.txt', 'r', "utf-8")
            print('Не совпадают')
            if fout1.read() != str(soup1.find(class_='last-update-date').string):  
                fout1 =  codecs.open('project/last_update_date1.txt', 'w+', "utf-8")                 
                fout1.seek(0)
                update_date_as_syte1 = soup1.find(class_='last-update-date').string
                send_in_telegram(update_date_as_syte1)
                fout1.write(update_date_as_syte1)
                fout1.close()
            elif fout2.read() != str(soup2.find(class_='last-update-date').string):
                fout2 =  codecs.open('project/last_update_date2.txt', 'w+', "utf-8")
                fout2.seek(0)
                update_date_as_syte2 = soup2.find(class_='last-update-date').string
                send_in_telegram(update_date_as_syte2)
                fout2.write(update_date_as_syte2)
                fout2.close()

        else:
            fout1.close()
            print('Одинаковые')
    else:
        print(f'1={response1.status_code},2={response2.status_code}')




def send_in_telegram(mesege_for_telegram):
    print(f'Запущен{mesege_for_telegram}')
    url = f'https://api.telegram.org/bot{config.token}/sendMessage'
    data = {'chat_id': config.channel_name, 'text': mesege_for_telegram}
    response = requests.post(url, data).json()
    print(response)



parsing_date()