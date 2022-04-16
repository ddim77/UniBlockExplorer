import string
import hashlib
import json

IP_LIST_FILE = "ip_list.dat"

# Проверка IP на валидность

def ip_valid(ip):
    parts = ip.split(".")
    if len(parts) != 4: return False
    for part in parts:
        if part.isdigit() and part[0] != '0' and int(part) in range(0, 256):
            pass
        else:
            return False
    return True

# Получаем список IP для работы из файла IP_LIST_FILE

with open(IP_LIST_FILE) as file:
    for line in file:
        ip = line.strip()
        if not ip_valid(ip):
            print(f"WARN: wrong ip {ip} in file {IP_LIST_FILE}")
        else:
            print(f"INFO: work with ip {ip}")











dict = {
    "name": "Villa",
    "balance": 1335,
    "active": True
}

list = ["exel", "mojo", "intro"]

binary1 = json.dumps(dict, sort_keys=True).encode()
binary2 = json.dumps(list, sort_keys=True).encode()

print(hashlib.sha256(binary1).hexdigest())

