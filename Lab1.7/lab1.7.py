import re, json, time, paramiko, pprint
from ipaddress import IPv4Address
import requests, ssl, socket
Login = 'restapi'
Password = 'j0sg1280-7@'
HTTPSport = '55443'
Console_IPAddress = '10.31.70.209'
REST_IPAddress = '10.31.70.210'
BUF_SIZE = 200
'''
# Задача 1 paramiko ------------------------------------------------------------------------------
BUF_SIZE = 50
TIMEOUT = 2

# Создаем объект — соединение по ssh
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Инициируем соединение по ssh
ssh_connection.connect(hostname="10.31.70.209", username='restapi', password='j0sg1280-7@', port=22, banner_timeout=100, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
time.sleep(TIMEOUT)

session.send("\n")
session.recv(BUF_SIZE)
session.send("show run\n")
time.sleep(TIMEOUT*2)
s = session.recv(BUF_SIZE).decode()
time.sleep(TIMEOUT*30)
session.close()
'''
# Задача 2 REST ------------------------------------------------------------------------------
url = 'https://10.31.70.210:55443'
r = requests.post('https://10.31.70.210:55443' + '/api/v1/auth/token-services', auth=("restapi", "j0sg1280-7@"), verify=False)
token = r.json()['token-id']
header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get('https://10.31.70.210:55443' + '/api/v1/interfaces', headers=header, verify=False)
pprint.pprint(r.json())



'''
print(r.status_code)

token = r.json()['token-id']

header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get(host_url + '/api/v1/interfaces', headers=header, verify=False)
pprint.pprint(r.json())
'''