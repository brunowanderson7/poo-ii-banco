import socket


ip = 'localhost'
port = 8000
addr = ((ip, port))

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(addr)


while True:
    try:
        menssage = input("Digite a mensagem a ser enviada: ")
        clientSocket.send(menssage.encode())
        print("Mensagem enviada!!")

        if menssage == 'Exit':
            clientSocket.close()
            break


        menssage = clientSocket.recv(1024).decode()

    except:
        clientSocket.close()
        print("Erro de comunicação!!")
    
    finally:
        if menssage == 'Exit':
            clientSocket.close()
            print("Conexão encerrada!!")
            break

        else:
            print("Mensagem recebida: {}" .format(menssage))