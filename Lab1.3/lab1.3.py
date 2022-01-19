from pysnmp.hlapi import * # Импортировать только High-level API

snmp_object1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной для коммутатора Cisco
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной для коммутатора Cisco


result1 = getCmd(SnmpEngine(), CommunityData('public', mpModel=0), #Запрос данных с устройства Cisco 10.31.70.107 через порт 161 имя Commubity - 'public' по имени MIB
				UdpTransportTarget(('10.31.70.107', 161)), ContextData(),
				ObjectType(snmp_object1))
print("Версия ПО на устройстве с адресом 10.31.70.107:")
print("_______________________________________________\n")
for param1 in result1:			#----------------------------------------------
	for param2 in param1[3]:	#Вывод версии ПО устройства Cisco 10.31.70.107
		print(param2)			#----------------------------------------------

result2 = nextCmd(SnmpEngine(), CommunityData('public', mpModel=0), #Запрос данных с устройства Cisco 10.31.70.107 через порт 161 имя Commubity - 'public' по значению MIB
				UdpTransportTarget(('10.31.70.107', 161)), ContextData(),
				ObjectType(snmp_object2), lexicographicMode=False) # Не идти в глубину

print("\nПеречень интерфейсов на устройстве 10.31.70.107:")
print("_______________________________________________")
for param3 in result2:							#------------------------------------------------------
	for param4 in param3[3]:					#
		param4 = str(param4)						#Вывод список интерфейсов с устройства Cisco 10.31.70.107
		if param4.find('Fast') > 0:				#
			print(param4[param4.find('Fast'):])		#------------------------------------------------------
