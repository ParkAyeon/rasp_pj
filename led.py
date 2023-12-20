import cv2
import dlib
from scipy.spatial import distance
import serial  
import time

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
ser = serial.Serial('/dev/ttyACM0', 9600)  

prev_eye_state = "open"

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        left_eye = []
        right_eye = []

        for n in range(42, 48):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            left_eye.append((x, y))

        for n in range(36, 42):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            right_eye.append((x, y))

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        #ear = (left_ear + right_ear) / 2.0

        if left_ear < 0.2 and right_ear < 0.2 and prev_eye_state == "open":
            print("Left&Right Blinking detected!")
            prev_eye_state = "closed"
        elif left_ear >= 0.2 and right_ear >= 0.2 and prev_eye_state == "closed":
            print("Left&Right eyes opened again!")
            # Do something when eyes open again
            ser.write(b'1')
            prev_eye_state = "open"
            #time.sleep(1)

        if left_ear < 0.2 and right_ear >= 0.2 and prev_eye_state == "open":
            print("Left eye blinked")
            prev_eye_state = "leftclosed"
        elif left_ear >= 0.2 and right_ear >= 0.2 and prev_eye_state == "leftclosed":
            print("Left eye opened again!")
            ser.write(b'2')
            prev_eye_state = "open"
            #time.sleep(1)

        if right_ear < 0.2 and left_ear >= 0.2 and prev_eye_state == "open":
            print("Right eye blinked")
            prev_eye_state = "rightclosed"
        elif right_ear >= 0.2 and left_ear >= 0.2 and prev_eye_state == "rightclosed":
            print("Right eye opened again")
            ser.write(b'3')
            prev_eye_state = "open"
            #time.sleep(1)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        ser.write(b'0')  
        break

cap.release()
cv2.destroyAllWindows()

