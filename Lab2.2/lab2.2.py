from flask import Flask, jsonify # импорт Flask, jsonify из библиотеки flask
import glob, re  # импорт библиотек glob, re
hostlist = {}
hostiplist= {}
configfiles = glob.glob("C:\Temp\config_files\*.txt") # Переменная для хранения списка файлов для анализа
def gethostslistfunc(configfiles): # Создаем функцию для поиска в файлах строк удовлетворящих нашим регулярным выражениям
    for configfile in configfiles:  # Цикл последовательного перебора анализируемых файлов
        with open(configfile, 'r') as f: # Открытие файла для последующего работы с ним
            hostip = []
            for line in f:
                line = line.strip()
                if bool(re.match(r'^hostname\s.+$', line)): # поиск строки наинающейся со слова "hostname"
                    hostname = re.match(r'^hostname\s.+$', line)
                    hostname = str(hostname.group())[9:]
                    hostlist[len(hostlist)] = hostname # формирование словаря содержащего ключ:значение вида 0:hostname (словарь всех hostname из всех анализируемых файлов)                                                           #
                if bool(re.match(r'^ip\saddress\s[\d]+\.[\d]+\.[\d]+\.[\d]+\s[\d]+\.[\d]+\.[\d]+\.[\d]+$', line)):    # поиск строки вида "ip address xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy"
                    var = re.match(r'^ip\saddress\s[\d]+\.[\d]+\.[\d]+\.[\d]+\s[\d]+\.[\d]+\.[\d]+\.[\d]+$', line)
                    var = var.group().split()
                    hostip.append(var[2])
                    hostiplist[hostname] = hostip # формирование словаря содержащего ключ:список вида hostname:[ip address1, ip address2] (словарь hostname:IP1,IPn из всех анализируемых файлов)
    return hostlist, hostiplist

hostlist, hostiplist = (gethostslistfunc(configfiles)) # вызов функции classfunc для поиска в файлах данных по заданным шаблонам


app = Flask(__name__) #создание веб-сервера
@app.route('/') # корневая страница - хелп
def index():
    help = {1:"Справочник функций REST!", 2:'-------------------------------------------------------------------------------', 3:"/configs - выводит на экран список имен hostname для всех устройств", 4:"/configs/hostname - выводит на экран список IP адресов для выбранного hostname"}
    #return "Справочник функций REST!" - вывод на экран текста "Справочник функций REST!"
    return jsonify(help) # вывод несколько строк из переменной help в виде JSON текста
@app.route('/configs') # страница - configs
def hostlistprint():
    return jsonify(hostlist) # вывод на экран списка имен hostname из всех файлов
@app.route('/configs/<hostname>') # страница - /configs/hostname, где переменная hostname принимает значение, введенное пользователем в адрсеной строке
def iplistprint(hostname):
    return jsonify(hostiplist[hostname]) # вывод на экран списка IP адресов для данного hostname

if __name__ == '__main__':  #проверка, что веб сервер запущен из тела нашей программы
    app.run(debug=True)     #запуск веб-сервера
