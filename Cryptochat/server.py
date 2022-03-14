import socket
import xor

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 1000))
clients = []  # Массив где храним адреса клиентов
print('Start Server')
key = '1234567890'
while 1:
    try:
        data, addres = sock.recvfrom(1024)
        data2 = xor.decrypt(key, data.decode('utf-8'))
    except Exception as e:
        print('ошибка получения' + str(e))
    else:
        print(data2)
        # print(addres[0], addres[1])
        if addres not in clients:
            clients.append(addres)  # Если такого клиента нету , то добавить
        for client in clients:
            if client == addres:
                continue  # Не отправлять данные клиенту, который их прислал
            sock.sendto(data, client)
