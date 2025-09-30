# dns_client.py
import socket

def dns_client(server_host='localhost', server_port=9999, timeout=5):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(timeout)

    try:
        hostname = input("Enter hostname (e.g., www.google.com): ").strip()
        if not hostname:
            print("No hostname entered. Exiting.")
            return

        client_socket.sendto(hostname.encode(), (server_host, server_port))

        try:
            data, _ = client_socket.recvfrom(4096)
            print(f"IP Address of {hostname}: {data.decode()}")
        except socket.timeout:
            print(f"No response from server at {server_host}:{server_port} (timeout {timeout}s).")
    except KeyboardInterrupt:
        print("\nClient cancelled.")
    except Exception as e:
        print("Client error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    dns_client()
