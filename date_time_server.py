import socket
import datetime

def date_time_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Date/Time Server is running on port 12345...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.send(current_datetime.encode())
        print(f"Sent: {current_datetime}")
        conn.close()

if __name__ == "__main__":
    date_time_server()

