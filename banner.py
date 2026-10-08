import socket
s = socket.socket()
s.settimeout(3)
s.connect(("192.168.1.1", 80))
s.send(b"GET / HTTP/1.0\r\n\r\n")
print(s.recv(1024).decode(errors="ignore"))
s.close()
