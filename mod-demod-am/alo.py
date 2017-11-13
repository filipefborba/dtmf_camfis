# Camada Física da Computação
# Exemplo socket server
## https://pymotw.com/2/socket/tcp.html

import socket
import sys


class TextGetter():
    def __init__(self, porta):
        self.porta = porta
        self.aberto = False

    def initialize_socket(self, porta):

        print("Inicializando socket TCP/IP")
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        self.server_address = ('localhost', self.porta)
        print("PORTA {}".format(self.porta))
        self.sock.bind(self.server_address)

        # Listen for incoming connections
        self.sock.listen(1)
        self.aberto = True

    def getText(self):
        if self.aberto == False:
            return "Abra o socket"
        else:
            while True:
                # Wait for a connection
                print("waiting for a connection")
                self.connection, self.client_address = self.sock.accept()

                try:
                    print(" connection from {}".format(client_address))

                    # Receive the data in small chunks and retransmit it
                    while True:
                        data = self.connection.recv(16)
                        if len(data) > 0:
                            print("{}".format(str(data, 'utf-8')), end="")
                            frase = str(data, 'utf-8')
                            return frase
                        # if(len(data) <= 0):
                        #     break