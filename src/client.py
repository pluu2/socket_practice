import socket
import pickle
class client (): 
    def __init__(self,ip,port): 
        self.ip=ip
        self.port=port
        self.s=0
    def createsocket(self): 
        self.s=socket.socket() 
        print("socket created")
    def connect(self): 
        self.s.connect((self.ip,self.port))
        print('connected')
        
        
        data = b''
        print('receiving')
        
        print ('.')
        block=self.s.recv(1000000) #this has to be adjusted for image
        data= block    
        self.s.close() 
        #print(data)
        #image=pickle.loads(data)
        return data
