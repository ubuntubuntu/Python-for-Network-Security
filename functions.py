def contains(sequence,item):
    toFind = False
    for element in sequence:
        if element == item:
            toFind = True
            break
    if toFind == True:
        print("The squence contains" ,item)
    else:
        print("The squence doesn't contain",item)     

contains([200,300,400,500],400)
contains([200,300,400,500],500)
contains([200,300,400,500],100)