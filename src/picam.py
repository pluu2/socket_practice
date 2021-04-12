import time
import picamera
import numpy as np
import pickle

class camera():
    def __init__(self,resolution=300): 
        self.camera=picamera.PiCamera()
        self.resolution=resolution
        self.camera.resolution=(320,304)
    def takePhoto(self): 
        self.camera.start_preview()
        time.sleep(2) 
        output=np.empty((320,304,3))
        #self.camera.PiArrayOutput(output,'rgb')
        self.camera.capture('temp.jpg')
               
        #return output

