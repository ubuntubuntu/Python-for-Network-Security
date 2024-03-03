try:
    print("10/0 :",str(10/0))
except Exception as exception:
    print("Error :", str(exception))

try:
    f = open('fil.txt',"r")
    print(f.read())
except Exception as exception:
    print("Error :", str(exception))