# dns_client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # send query to server (make sure this port matches the server's bind port)
    client.sendto(b'youtube.com', ('localhost', 1025))

    # receive response
    ip, _ = client.recvfrom(4096)
    print('IP Address:', ip.decode())
except ConnectionResetError:
    print("No server listening at that address/port (ICMP Port Unreachable received).")
except Exception as e:
    print("Client error:", e)
finally:
    client.close()
