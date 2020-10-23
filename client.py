
import socket

# definicao do ip e da porta
IP = "127.0.0.1"
PORT = 3030

# estabelecimento da conexao
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))

# loop para rodar enquanto o chat nao for terminado
while 1:
    try:
        # usuario digita mensagem
        mensagem = input('Digite uma mensagem:')
        # envio mensagem codificada para o servidor 

        clientSocket.send(mensagem.encode())
       
        # recebo mensagem do servidor e decodifico
       
        mensagemDoServidor = clientSocket.recv(1024).decode()
        if mensagemDoServidor == 'Conexao Finalizada':
            break 

        # exibo mensagem do servidor na tela
        print('Servidor:', str(mensagemDoServidor))
    except:
        break

# fecho o socket do client
clientSocket.close()