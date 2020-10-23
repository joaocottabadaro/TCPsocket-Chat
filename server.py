
import socket

# configuracao do ip e da porta
ip = 'localhost'
serverPort = 3030

# inicializacao do servidor
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverSocket.bind((ip,serverPort))
serverSocket.listen()


# print para verificar se o servidor inicializou
print('Servidor Rodando')

# loop infinito para rodar o servidor
while 1:

    try:
    # aceito conexao com o client, recebo 2 valores, um objeto para enviar e receber dados e o endereco da conexao
        clientSocket, addr = serverSocket.accept()

        # loop para continuar a troca de mensagens 
        while 1:
            # recebo mensagem do cliente e decodifico
            mensagemCliente = clientSocket.recv(1024).decode()

            # keyword * para o client desligar o servidor, 
            if mensagemCliente == '*':
                clientSocket.send('Conexao Finalizada'.encode())
                break
            else:
                # exibe na tela a mensagem do client
                print('Client: ', str(mensagemCliente))

                    # servidor digita uma mensagem,  envio a mensagem para o client codificada
                mensagemServidor = input('Digite uma resposta:')
                clientSocket.send(mensagemServidor.encode())

        # servidor fecha de acordo com o pedido do client(pelo break do if)
        serverSocket.close()
        # caso ocorra algum erro inesperado o servidor E finalizado e o loop infinito E terminado
    except:
        serverSocket.close()
        break
    
    
 
    
