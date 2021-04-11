import sysconfig 

from sysconfig import port
import src.server 
from src.server import server

newserver=server(port) 
newserver.createsocket()
newserver.listen()

