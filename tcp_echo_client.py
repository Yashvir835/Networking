import socket

def tcp_echo_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 12345)
    print(f"Connecting to {server_address[0]} port {server_address[1]}")
    client_socket.connect(server_address)

    try:
        # Send data
        message = input("Enter message to send to server: ")
        print(f"Sending: {message}")
        client_socket.sendall(message.encode())

        # Receive the same data back (echo)
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

    finally:
        # Close the connection
        print("Closing socket")
        client_socket.close()

if __name__ == "__main__":
    tcp_echo_client()
