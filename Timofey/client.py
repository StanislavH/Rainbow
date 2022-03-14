import socket
import threading

def read_sok():
    while 1:
        data = sor.recv(1024)
        print(data.decode('utf-8'))

key = '1234567890'
server = '192.168.0.53', 7777  # Данные сервера
name = input("Введите имя:")  # Вводим наш псевдоним
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))  # Задаем сокет как клиент
sor.sendto((name + ' Connect to server').encode('utf-8'), server)  # Уведомляем сервер о подключении
potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    mensahe = input()
    sor.sendto(('[' + name + ']:' + mensahe).encode('utf-8'), server)
