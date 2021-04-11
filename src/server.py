import socket
import picamera
import picam
from picam import camera
import numpy as np
#will listen.

class server() : 
    def __init__(self,port): 

        self.port=port
        self.s=0
        self.cam=camera() #the camera
    def createsocket(self): 
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print('socket successfully created')
    
    #start to listen.
    def listen (self): 
      self.s.bind(('',self.port))
      print("socket bound to %s" %(self.port))
      self.s.listen(5) 
      print("socket is listening") #continually searches.
      while True: 
        c, addr = self.s.accept()     
        print ('Got connection from', addr )
        output=self.takePhoto().flatten()

        c.send(output)
        c.close()

    def takePhoto(self): 
        return self.cam.takePhoto()
    

        
    

