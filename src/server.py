import socket

#will listen.

class server() : 
    def __init__(self,port): 

        self.port=port
        self.s=0
    def createsocket(self): 
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print('socket successfully created')
    
    #start to listen.
    def listen (self): 
      self.s.bind(('',self.port))
      print("socket bound to %s" %(self.port))
      self.s.listen(5) 
      print("socket is listening")
      while True: 
        c, addr = self.s.accept()     
        print ('Got connection from', addr )
        c.send("Thank you for conneting")
        c.close()


    

        
    

