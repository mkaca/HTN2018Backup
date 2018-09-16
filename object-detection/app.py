import os
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import time
from flask import Flask, render_template, request,jsonify,send_file

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

model_path = "MobileNetSSD_deploy.caffemodel"
prototxt_path = "MobileNetSSD_deploy.prototxt.txt"

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
test_dict = {}

def detect_objects(image):

	frame = imutils.resize(image, width=400)
	 
	# grab the frame dimensions and convert it to a blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),0.007843, (300, 300), 127.5)
	 
	# pass the blob through the network and obtain the detections and
	# predictions
	net.setInput(blob)
	detections = net.forward()

	for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the prediction
		confidence = detections[0, 0, i, 2]
	 
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > 0.2:
			# extract the index of the class label from the
			# `detections`, then compute the (x, y)-coordinates of
			# the bounding box for the object
			idx = int(detections[0, 0, i, 1])

			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int") 

			label = "{}: {:.2f}% : {} : {} : {} : {}".format(CLASSES[idx], confidence * 100, startX, startY, endX, endY)
			
			print("[INFO] {}".format(label))
			cv2.rectangle(frame, (startX, startY), (endX, endY),COLORS[idx], 2)
			y = startY - 15 if startY - 15 > 15 else startY + 15
			cv2.putText(frame, CLASSES[idx], (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)


	#return test_dict
	cv2.imwrite('detected_images/image.jpeg', frame)
	return send_file('detected_images/image.jpeg', attachment_filename='image.jpeg')



app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	image = request.files['image']
	filename = os.path.join(app.config['UPLOAD_FOLDER'], "image.jpeg")
	image.save(filename)
	image = cv2.imread('uploads/image.jpeg')
	description = detect_objects(image)
	
	#return jsonify(description)
	return description
	return render_template('index.html')