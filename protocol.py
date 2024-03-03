class protocol(object): # we have to put word class to define that it is a class
    def __init__(self,name,number,description): # its mandatory to put __init__ after word def
        self.name = name
        self.number = number
        self.description = description

class vulnerability(object):
    def __init__(self,name,cve,description):
        self.name = name
        self.cve = cve
        self.description = description