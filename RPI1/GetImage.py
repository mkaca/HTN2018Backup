from picamera import PiCamera
import time
import socket
from PIL import Image
import numpy

camera = PiCamera()

camera.start_preview()
time.sleep(1)
camera.capture('/home/pi/Desktop/HTN2018/RPI1/TestImg.jpg')
camera.stop_preview()
time.sleep(2)
imgData = Image.open('/home/pi/Desktop/HTN2018/RPI1/TestImg.jpg')
imgData = numpy.array(imgData)
print (imgData)

s = socket.socket()
port = 12456
s.settimeout(5)

s.connect(("169.254.244.191",port))
strImgData = str(imgData)
print("done connecting")
s.sendall(strImgData)

print(s.recv(1024))
s.close
