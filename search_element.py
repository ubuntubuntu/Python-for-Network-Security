protocolList=["ftp","http","icmp","vpn"]
toFind = "vpn"
found = False
for i in range(len(protocolList)):
    found = protocolList[i] == toFind
    if found ==  True:
        break
if found == True:
    print("Element found at index", i)
else:
    print("Element not found")

