import socket
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
        print(self.s.recv(1024))
        self.s.close() 
