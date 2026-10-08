import socket
target = "192.168.1.3"
print(f"Scanning {target} ...\n")
for port in [21,22,23,80,443,8080]:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((target, port))
        print(f"[OPEN] Port {port} kebuka!")
        s.close()
    except:
        print(f"[CLOSED] Port {port} ketutup")
print("\nSelesai bro!")
