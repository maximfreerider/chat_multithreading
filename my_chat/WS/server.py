import socket
import time

""" Наш сервер только принимает и отправляет сообщения,
    шифруем инфу на клиенте"""

host = '127.0.0.1'
port = 9090

# наш список клиентов, ИХ АДРЕССА
clients = []

# наши сокеты , первый - ip, второй - гвз
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#  поднимаем сервак на этом хоте и порте
s.bind((host, port))

quit = False
print("[ Server is started ]")

# пока сервер запущен
while not quit:

    try:
        """ data - сообщение, которое отправляет пользователь, 
            addr - то что сервак принимает, например 39705 - по сути айдишка(личный адрес) юзера """
        data, addr = s.recvfrom(1024)
        """1024 байта, соответственно сервак может 
            принимать по одному килобайту """
        # если новый юзер, то присваиваем ему адресс
        if addr not in clients:
            clients.append(addr)

        """ для того что бы выдеть когда было отправлено сообщение или когда добавился юзер """
        it_is_a_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        # addr[0] - ip, addr[1] - user`s addr, and show time when user join, go out or write a message
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + it_is_a_time + "]/", end=" ")

        print(data.decode("utf-8"))

        # что бы не отправлять самому себе сообщения, т.е.,
        # по сути я отправляю своё сообщение всем кроме себя
        for client in clients:
             if addr != client:
                # отправляю всем своё сообщение
                s.send(data, client)
    except:
        print("\n [Server Stopped]")
        # если нажму ctrl + c - то сервак остановится в итоге udp\ip просто закроется
        quit = True

s.close()