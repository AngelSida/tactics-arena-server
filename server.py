# server.py
import socket, threading

clients = []

def relay(c):
    while True:
        try:
            data = c.recv(10_000_000)
            if not data:
                break
            for other in clients:
                if other != c:
                    other.sendall(data)
        except:
            break

s = socket.socket()
s.bind(("0.0.0.0", 9999))
s.listen(2)
print("Server running")

while True:
    c, _ = s.accept()
    clients.append(c)
    threading.Thread(target=relay, args=(c,), daemon=True).start()

