import sysconfig 

from sysconfig import port
import src.server 
from src.server import server

import picamera
import src.picam
from src.picam import camera

newserver=server(port) 
newserver.createsocket()
newserver.listen() #waits for the main computer 


