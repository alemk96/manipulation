import threading
import cv2
import logging
import subprocess
import os
from deepface import DeepFace

logging = logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter  = 0
face_match = False
reference_img = cv2.imread('reference.png')

def check_face(frame):
    logging.debug("Checking face")
    global face_match
    logg
    '''    global face_match
    
    reference_img = cv2.imread('reference.png')
    result = DeepFace.verify(frame, reference_img.copy())['verified']
    try:
        if result:
            face_match = True
        else:
            logging.debug("Not a match")
            face_match = False
    except ValueError:
        face_match = False
    '''


while True:
    ret, frame = cap.read()
    thread = threading.Thread(target=check_face, args=(frame,))
    if ret :
        if counter % 30 == 0:
            try:
                thread.start()
            except ValueError:
                pass  
        counter += 1
        
        if face_match: 
            cv2.putText(frame, "Match", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
        else:
            # BGR è il profilo colore di OpenCV
            cv2.putText(frame, "Not a Match", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        cv2.imshow('Acquired image', frame)
        
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()
