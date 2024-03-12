import numpy as np
import socket

host = "84.237.21.36"
port = 5152

def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        data.extend(packet)
    return data

#функция, которая возвращает плоский массив, содержащий элементы, расположенные вокруг указанных координат y, x в матрице b
def arrayb(b, row, col):
    return b[row-1:row+2, col-1:col+2].flatten()

#находим максимум
def maximum(data):
    pos1, pos2 = None, None
    for y in range(1, data.shape[0] - 1):
        for x in range(1, data.shape[1] - 1):
            l = data[y, x]
            if l < 3: continue
            if any([n > l for n in arrayb(data, y, x)]): 
                continue
            if pos1 is None: pos1 = (x, y)
            elif pos2 is None: pos2 = (x, y)
            else: 
                break
    return pos1, pos2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    for i in range(10):
        sock.send(b"get")
        bts = recvall(sock, 40002)
        im = np.frombuffer(bts[2:40002], dtype="uint8").reshape(200, 200)
        pos1, pos2 = maximum(im)
        res = np.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
        sock.send(f"{res:.1f}".encode())
        print(sock.recv(20).decode())
    sock.send(b"beat")
    print(sock.recv(20).decode())