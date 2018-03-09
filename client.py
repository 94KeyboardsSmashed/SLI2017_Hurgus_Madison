import socket

HOST = '192.168.1.6'
PORT = 50007

BUFF_SIZE = 1024

def sendData(sock, text):
    sock.sendall(text)
    data = s.recv(BUFF_SIZE)
    print("SENT: {0: >30} -> RECVD: {1}".format(text, data))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

sendData(s, "Hello!")
sendData(s, "How are you?")
sendData(s, "OK, then...")
sendData(s, "Bye")

s.close()
