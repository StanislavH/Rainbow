import socket
import threading
import xor


def read_sok():
    while 1:
        try:
            data = sor.recv(1024)
            data = xor.decrypt(key, data.decode('utf-8'))
        except Exception as e:
            print('ошибка получения'+str(e))
        else:
            print(data)

        # print(data.decode('utf-8'))


key = '1234567890'
server = '192.168.0.181', 1000  # Данные сервера
server='127.0.0.1',1000
name = input("Введите имя:")  # Вводим наш псевдоним
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))  # Задаем сокет как клиент
s = xor.encrypt(key, (name + ' Connect to server')).encode('utf-8')
sor.sendto(s, server)  # Уведомляем сервер о подключении
potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    try:
        mensahe = input()
        s = xor.encrypt(key, ('[' + name + ']:' + mensahe)).encode('utf-8')  # Я ШАС МИКРОФОН СЪЕМ!!!
        sor.sendto(s, server)
    except Exception as e:
        print('ошибка отправки' + str(e))
