import sysconfig 
from sysconfig import port

import src.picam  
from src.picam import camera

import numpy as np
import src.server 
from src.server import server

newserver=server(port) 
newserver.createsocket()
newserver.listen() #waits for the main computer 
