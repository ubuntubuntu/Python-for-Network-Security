protocol = {"ftp":21,"http":80,"ldap":389,"ssh":22}
print(protocol)
protocol["ftp"] = 210
print(protocol) 
keys = protocol.keys()
print(keys)
ite = protocol.items()
print(ite)
ite.sort()
for key,value in ite:
    print(key,value)
protocol["ldap"] = 389
print(protocol)

