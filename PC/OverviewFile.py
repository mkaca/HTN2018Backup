
##### This creates the socket SERVER #####

import socket
import cv2
import time
import numpy
import json

lCamActive = True
rCamActive = True

leftCameraSocket = socket.socket()
leftCameraSocket.settimeout(40)
rightCameraSocket = socket.socket()
rightCameraSocket.settimeout(40)
print ('socket instances created')

# reserve PORT so that it's not in use by something else:
portL = 12450  # 10.21.1.137:1...INTERNET...ETHERNET: 169.254.X.X...current: .138.153
portR = 12553  # 10.21.120.156:1...INTERNET...ETHERNET: 169.254.X.X...current: .87.52

# Bind it to the port
# Note that we have not typed any IP into the IP field..... we input an empty string ... this makes server
#     listen to requests coming from other computers on network
if lCamActive: 
	leftCameraSocket.bind(('', portL))
if rCamActive:
	rightCameraSocket.bind(('',portR))
print("socket binded to left port:%s and right port: %s"%((portL),(portR)))

# make server listen to requests
if lCamActive:
	leftCameraSocket.listen(5)  # where 5 = max number of queued connections
	print('left socket is listening')
if rCamActive:
	rightCameraSocket.listen(5)
	print('right socket is listening')

#establish connection with client
if lCamActive:
	cL, addrL = leftCameraSocket.accept()
	print ('got connection from left socket', addrL)
if rCamActive:
	cR, addrR = rightCameraSocket.accept()
	print ('got connection from right socket', addrR)


### WHILE LOOP STARTS HERE

if lCamActive:
	chunks = []
	bytes_recd = 0
	maxBytes = 240*240*3
	while bytes_recd < (maxBytes):
		chunk = cL.recv(min((maxBytes - bytes_recd), 16384))
		if chunk == b'':
			raise RuntimeError("socket connection broken L")
		chunks.append(chunk)
		bytes_recd = bytes_recd + len(chunk)
		print(bytes_recd)
	imageData = b''.join(chunks)
	fromBufferL = numpy.frombuffer(imageData, dtype=numpy.uint8, count= -1)
	fromBufferL = fromBufferL.reshape(240,240,3)

if rCamActive:
	chunks = []
	bytes_recd = 0
	maxBytes = 240*240*3
	while bytes_recd < (maxBytes):
		chunk = cR.recv(min((maxBytes - bytes_recd), 16384))
		if chunk == b'':
			raise RuntimeError("socket connection broken R")
		chunks.append(chunk)
		bytes_recd = bytes_recd + len(chunk)
		print(bytes_recd)
	imageData = b''.join(chunks)
	fromBufferR = numpy.frombuffer(imageData, dtype=numpy.uint8, count= -1)
	fromBufferR = fromBufferR.reshape(240,240,3)

#print(numpy.shape(fromBuffer))
#print (type(fromBuffer))
#print(fromBuffer)


#send a response to the client and then close
if lCamActive:
	cL.send(('Thank you for connecting').encode())
	cL.close()
if rCamActive:
	cR.send(('Thank you for connecting').encode())
	cR.close()

leftCameraSocket.close()
rightCameraSocket.close()

if lCamActive:
	cv2.imshow('testL',fromBufferL)
if rCamActive:
	cv2.imshow('testR',fromBufferR)
cv2.waitKey(0)




#### Once sanity check / speed is complete....

#Run opencv stereo vision and test how it looks like

