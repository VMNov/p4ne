import glob
from ipaddress import IPv4Address
AddressList = []
configfiles = glob.glob("C:\Temp\config_files\*.txt")
for i in configfiles:
    with open(i) as configfile:
        for txtstr in configfile:
            txtstr = txtstr.strip()
            if ('ip address' in txtstr) and (len(txtstr.split()) == 4):
                txtstr = txtstr.split()
                if IPv4Address(txtstr[2]).version == IPv4Address(txtstr[3]).version:
                    AddressList.append(f'{txtstr[0]} {txtstr[1]} {txtstr[2]} {txtstr[3]}')
i = 0
AddressListSort = list(set(AddressList))
while i < len(AddressListSort):
    print(AddressListSort[i])
    i += 1
print(f'Кол-во уникальных IP адресов = {len(AddressListSort)}')