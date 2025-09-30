import socket

def date_time_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    data = client_socket.recv(1024).decode()
    print(f"Current Date and Time from Server: {data}")
    client_socket.close()

if __name__ == "__main__":
    date_time_client()
