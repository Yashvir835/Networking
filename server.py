import socket

def dns_server(host='localhost', port=9999):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"DNS Server is running on {host}:{port} (UDP) — press Ctrl+C to stop")

    try:
        while True:
            data, addr = server_socket.recvfrom(4096)
            hostname = data.decode().strip()
            print(f"Received request from {addr}: {hostname}")

            try:
                ip_address = socket.gethostbyname(hostname)
            except socket.gaierror:
                ip_address = "Hostname not found"

            server_socket.sendto(ip_address.encode(), addr)
            print(f"Sent to {addr}: {ip_address}")
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    dns_server()
