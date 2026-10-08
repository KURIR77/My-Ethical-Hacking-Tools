import requests, re
r = requests.get("http://192.168.1.1", timeout=3)
judul = re.search("<title>(.*?)</title>", r.text, re.I)
if judul:
    print(f"Judul halaman: {judul.group(1)}")
else:
    print("Gak ada judul, ini halaman login ZTE")
print(f"Status: {r.status_code} - Siap di-audit!")
