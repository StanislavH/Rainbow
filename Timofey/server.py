import socket
import xor

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5050))
clients = []  # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    print(data)
    if addres not in clients:
        clients.append(addres)  # Если такого клиента нету , то добавить
    for client in clients:
        if client == addres:
            continue  # Не отправлять данные клиенту, который их прислал
        sock.sendto(data, client)
