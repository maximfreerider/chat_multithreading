import socket, threading, time

"""
threading нужен для реализации многопоточности,
т.е. если этого не будет то я смогу прочитать сообщение толлько тогда когда отправил своё
"""

#
key = 8194

shutdown = False
join = False

# name == self in OOP

def receiving(name, sock):
    """
    Реализуем функцию, которая будет принимать все данные от юзера,
    С помощью такой такой конструкции мы можем принимать сообщения о других юзеров
    try - except - для того, если выскочит ошибка во время многопоточности - то пропустить её
    """

    while not shutdown:
        try:
            while True:
                # принимаем сообщения с другого клиента
                data, addr = sock.recvfrom(1024)
                # print(data.decode("utf-8"))

                # дешифруем сообщение
                decrypt = ""; k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += 1
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                    print(decrypt)
                    # конец дешифровки
                    time.sleep(0.2)
        except:
            pass

host = '127.0.0.1'
port = 0

server = ("192.168.0.101", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
# для того что бы пользователь мог выйти из чата
s.setblocking(0)


user_name = input("Name : ")


rT = threading.Thread(target=receiving, args=("RecvThred", s))
rT.start()


# этот цикл(while) служит для отправки сообщений

# пока юзер не вышел
while shutdown == False:
    """если пользователь не присоединён, то отправляем на сервер сообщение
        [ip]=[addr]=[time/name] => joined chat"""
    if join == False:
        s.sendto(("["+user_name+"] => join chat ").encode("utf-8"), server)
        # подключаем юзера
        join = True
    else:
        try:
            message = input()

            # начало шифровки сообщения
            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt
            # конец шифровки сообщения

            if message != "":
                # отправка сообщения на сервер(айпишник, и порт)
                s.sendto(("[" + user_name + "] ::" + message).encode("utf-8"))
            # делаем задержку в 200 милисекунд между отправкой и приёмом сообщения
            time.sleep(0.2)
        except:
            # (Ctrl + C) если юзер вышел из чата, то отправляем об этом сообщение на сервер
            s.sendto(("[" + user_name  + "] <= left chat ").encode("utf-8"), server)
            # указываем что юзер вышел
            shutdown = True

rT.join()
s.close()


