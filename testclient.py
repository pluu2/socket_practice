import sys
import pickle
#print(sys.version)

import sysconfig 
import numpy as np
from sysconfig import ip,port
import src.client 
from src.client import client
import matplotlib as py
from matplotlib import pyplot as py

newclient =client(ip,port) 
newclient.createsocket()
temp=newclient.connect() #return a massive pickle file
print('received something')
print(temp)


#py.imshow(temp.reshape(320,304,3))
#i = np.arange(320*304).reshape(320, 304)

#nim=np.frombuffer(image, dtype=i.dtype)

#print(nim.shape)


