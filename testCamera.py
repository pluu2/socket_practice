import src.picam  
from src.picam import camera
import numpy as np

cam=camera()

test=cam.takePhoto()
print(test.shape)