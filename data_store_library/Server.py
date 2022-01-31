import socket
import tqdm
import os
from decouple import config

server_host = config('SERVER_HOST')
server_port = config('SERVER_PORT')
buffer_size = config('BUFFER_SIZE')
SEPARATOR = "   "

s = socket.socket()
s.bind((server_host, server_port))
s.listen(10)
print(f"[*] Listening as {server_host}:{server_port}")
print("Waiting for the client to connect... ")
client_socket, address = s.accept()
print(f"[+] {address} is connected.")
received = client_socket.recv(buffer_size).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(buffer_size)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))
client_socket.close()
s.close()