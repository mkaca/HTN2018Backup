import json
from picamera import PiCamera
import time
import socket
from PIL import Image
import numpy

camera = PiCamera()
camera.resolution = (240,240)
camera.start_preview()
time.sleep(1)
camera.capture('/home/pi/Desktop/HTN2018/RPI1/TestImg.jpg')
camera.stop_preview()
time.sleep(2)
imgData = Image.open('/home/pi/Desktop/HTN2018/RPI1/TestImg.jpg')
imgData = (numpy.array(imgData))
print (imgData)
print(numpy.shape(imgData))


s = socket.socket()
port = 12452
s.settimeout(8)

s.connect(("169.254.244.191",port))
strImgData = imgData.tostring()
bufferFlex = numpy.frombuffer(strImgData, dtype = numpy.uint8, count = -1)
print(numpy.shape(bufferFlex))
print(" ")
print("done connecting")
s.sendall(strImgData)

print(s.recv(2048))
s.close
