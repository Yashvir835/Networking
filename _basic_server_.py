import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(1)
print("Server is  Listening...")

conn,addr = server_socket.accept()
print("Connected with:",addr)

data = conn.recv(1024).decode()
print("Client says:",data)
conn.send('Hello client,message recived!'.encode())
conn.close()