import socket

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, address = s.accept()
print('Connected by', str(address))

while True:
    data = connection.recv(1024)
    if data.lower().strip() == "bye":
        connection.send("HANGUP")
        print("BYE!")
        break

    print("CALLER SAYS: " + str(data))
    connection.send("TX from " + str(address[0]) + " ACK")

connection.close()
