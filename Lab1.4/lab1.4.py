from ipaddress import IPv4Network #Импортируем библиотеку для работы с IP адресами
import random #Импортируем библиотеку случайных чисел

class IPv4RandomNetwork(IPv4Network):   #Создаем новый класс который унаследован от класса IPv4Network библиотеки ipaddress
    def __init__(self, network_address, netmask):
        IPv4Network.__init__(self, (network_address, netmask), strict=False)   #Передаем переменные из нашего класса в унаследованный класс для использования методов и функций данного класса
    def regular(self): # Создаем метод класса для возврата строки адреса сети/маска
        return (f'{self.network_address}/{self.netmask}')

NetList = []
NetListSize = 50

while NetListSize > 1: #Создаем цикл для формирования списка из 50 произвольных сетей
    network_address = random.randint(0x0b000000, 0xdf000000) #Генерируем произвольный адрес сети в дапазоне 0x0b000000, 0xdf000000
    netmask = random.randint(8, 24) #Генерируем произвольную маску сети в дапазоне 8-24
    net = IPv4RandomNetwork(network_address,netmask) #Создаем объект на основе нашего класса class IPv4RandomNetwork(IPv4Network)
    if net.is_global == True : # Проверяем принадлежность к публичной сети и добавляем в словарь
        NetList.append(net.regular())
        NetListSize -= 1
NetList.sort() #Выполняем сортировку
for net in NetList:  print(net) #Выводим отсортированный список сетей
