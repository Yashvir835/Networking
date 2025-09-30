import socket

def tcp_echo_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 12345)
    print(f"Starting up server on {server_address[0]} port {server_address[1]}")
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1) # Allow one queued connection

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        conn, addr = server_socket.accept()
        print(f"Connection from: {addr}")

        try:
            # Receive data from the client
            data = conn.recv(1024)
            print(f"Received from client: {data.decode()}")

            if data:
                # Send the received data back (echo)
                print(f"Sending back: {data.decode()}")
                conn.sendall(data)
            else:
                break # No more data from client, connection closed

        finally:
            # Clean up the connection
            print("Closing current connection")
            conn.close()

if __name__ == "__main__":
    tcp_echo_server()
