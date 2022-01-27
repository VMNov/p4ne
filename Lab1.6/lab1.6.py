import glob, re # импорт библиотек glob, re
iplist = {}         #---------------------------------
interfacelist = {}  # Переменные для хранения
hostlist = {}       #       результата
emptydict = {}      #----------------------------------
configfiles = glob.glob("C:\Temp\config_files\*.txt") # Переменная для хранения списка файлов для анализа
def classfunc(configfiles): # Создаем функцию для поиска в файлах строк удовлетворящих нашим регулярным выражениям
    for configfile in configfiles:  # Цикл последовательного перебора анализируемых файлов
        with open(configfile, 'r') as f: # Открытие файла для последующего работы с ним
            for line in f:                                                                                          #------------------
                line = line.strip()                                                                                 #
                if bool(re.match(r'^ip\saddress\s[\d]+\.[\d]+\.[\d]+\.[\d]+\s[\d]+\.[\d]+\.[\d]+\.[\d]+$', line)):    #
                    var1 = re.match(r'^ip\saddress\s[\d]+\.[\d]+\.[\d]+\.[\d]+\s[\d]+\.[\d]+\.[\d]+\.[\d]+$', line)   # Цикл для поиска в строке
                    iplist[len(iplist)] = var1.group()                                                              # файла следующих данных по маске:
                elif bool(re.match(r'^interface\s\w+Ethernet\d\/\d$', line)):                                       # ip address x.x.x.x x.x.x.x
                    var1 = re.match(r'^interface\s\w+Ethernet\d\/\d$', line)                                        # interface GigabitEthernetX/X
                    interfacelist[len(interfacelist)] = var1.group()                                                # hostname xxx
                elif bool(re.match(r'^hostname\s.+$', line)):                                                       #
                    var1 = re.match(r'^hostname\s.+$', line)                                                        #
                    hostlist[len(hostlist)] = var1.group()                                                          #
    return iplist, interfacelist, hostlist                                                                          #----------------------

def printfunc(printlist):       #---------------------------------------
    i = 0                       #
    while i < len(printlist):   #
        print(printlist[i])     # Функция для вывода результата работы
        i += 1                  # программы на экран
    if i > 0: i -= 1            #
    return i                    #---------------------------------------

iplist, interfacelist, hostlist = (classfunc(configfiles)) # вызов функции classfunc для поиска в файлах данных по заданным шаблонам

ipliststr = printfunc(iplist)               #-------------------------
interfaceliststr = printfunc(interfacelist) # Вызов функции printfunc для вывод на экран данных из iplist, interfacelist, hostlist
hostliststr = printfunc(hostlist)           #--------------------------
print(f"Кол-во IP адресов: {ipliststr}. Кол-во интерфейсов: {interfaceliststr}. Кол-во хостов: {hostliststr}")
