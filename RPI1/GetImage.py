import json
from picamera import PiCamera
import time
import socket
from PIL import Image
import numpy

print("starting code")
camera = PiCamera()
camera.resolution = (240,240)
s = socket.socket()
port = 12452
s.settimeout(8)
modulusBoi  = 12

check = True
while(True):
  if (int(str(datetime.datetime.now())[17:19]) % modulusBoi == 0):
    print ("starting timeCheck")
    break
time.sleep(0.1)
while (check):
  timeS = int(str(datetime.datetime.now())[21:24])
  print((timeS))
  timeB = int(str(datetime.datetime.now())[17:19]) 
  print(timeB)
  if (timeS == 0 and timeB % modulusBoi == 0):
      check = False
      print('breaking')

camera.start_preview()
time.sleep(0.4)
camera.capture('/home/pi/Desktop/HTN2018/RPI1/TestImg.jpg')
camera.stop_preview()
time.sleep(0.4)
imgData = Image.open('/home/pi/Desktop/HTN2018/RPI1/TestImg.jpg')
imgData = (numpy.array(imgData))
#print (imgData)
#print(numpy.shape(imgData))

s.connect(("169.254.244.191",port))
strImgData = imgData.tostring()
bufferFlex = numpy.frombuffer(strImgData, dtype = numpy.uint8, count = -1)
print(numpy.shape(bufferFlex))
print(" ")
print("done connecting")

bytesSend = 0
while bytesSend < (240*240*3):
  sent  = s.send(strImgData[bytesSend:])
  if sent == 0:
    raise RuntimeError("socket connection broken")
  bytesSend = bytesSend + sent
  print(bytesSend)

print(s.recv(2048))
s.close
