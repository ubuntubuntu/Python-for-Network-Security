from ftplib import FTP
from configparser import ConfigParser

CONF = 'config.ini'
config = ConfigParser()
config.read(CONF)

SERVER = config.get('aplikasiku','server')
username = config.get('aplikasiku','username')
password = config.get('aplikasiku','password')

ftp = FTP(SERVER)
ftp.login(user=username, passwd=password)
ftp.dir()
ftp.quit()
