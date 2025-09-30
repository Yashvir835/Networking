# dns_server.py
import socket

dns_records = {
    'youtube.com': '93.184.216.34',
    'google.com':  '142.250.190.14'
}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 1025))
print("DNS-like UDP server listening on localhost:1025")

try:
    while True:
        data, addr = server.recvfrom(4096)   # larger buffer just in case
        domain = data.decode().strip()
        print(f"Query from {addr}: {domain}")
        ip = dns_records.get(domain, 'Domain not found')
        server.sendto(ip.encode(), addr)
except KeyboardInterrupt:
    print("\nServer shutting down.")
finally:
    server.close()
