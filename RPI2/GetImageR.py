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
camera.capture('/home/pi/Desktop/HTN2018/RPI2/TestImgR.jpg')
camera.stop_preview()
time.sleep(2)
imgData = Image.open('/home/pi/Desktop/HTN2018/RPI2/TestImgR.jpg')
imgData = (numpy.array(imgData))
print (imgData)
print(numpy.shape(imgData))

s = socket.socket()
port = 12553
s.settimeout(8)

s.connect(("169.254.250.64",port))
strImgData = imgData.tostring()
bufferFlex = numpy.frombuffer(strImgData, dtype = numpy.uint8, count = -1)
print(numpy.shape(bufferFlex))
print(" ")
print("done connecting R")

bytesSend = 0
while bytesSend < (240*240*3):
  sent  = s.send(strImgData[bytesSend:])
  if sent == 0:
    raise RuntimeError("socket connection broken R")
  bytesSend = bytesSend + sent
  print(bytesSend)

print(s.recv(2048))
s.close
