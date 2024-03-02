# "key" : value, key must be unique but value doesnt have to
# we cannot change the key but we can change the value 
protocol = {"ftp":21,"http":80,"ldap":389,"ssh":22} # the dictionary of protocols (key) and the port number (value)
print(protocol)
protocol["ftp"] = 210 # we assign new protocol number in ftp
print(protocol) 
keys = protocol.keys() # we extract the keys from dictionary and save it into keys 
print(keys)
ite = protocol.items() # we extract the items from dictionary and save it into ite
print(ite)
for key,value in ite: 
    print(key,value)
protocol["ldap"] = 389
print(protocol)

