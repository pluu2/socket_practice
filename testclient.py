import sysconfig 

from sysconfig import ip,port
import src.client 
from src.client import client

newclient =client(ip,port) 
newclient.createsocket()
newclient.connect()

