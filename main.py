import numpy as np
import cv2
import yeelight
import time

IP = "192.168.11.3"
bulb = yeelight.Bulb(IP)
bulb.turn_on()
bulb.set_rgb(255, 255, 255)
bulb.set_brightness(100)
cap = cv2.VideoCapture(1)
sums =0
bulb.set_rgb(0, 0, 255)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (33,33), 1)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 60, param1=100, param2=29, minRadius=13, maxRadius=20)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,0,255),2)
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            sum = (len(circles[0,:]))
            cv2.putText(frame, 'Lending Now', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), thickness=5)
            try:
                if sum != sums:
                    bulb = yeelight.Bulb(IP)
                    time.sleep(.5)
                    bulb.set_brightness(100)
                    if sum == 1:
                        bulb.set_rgb(255, 255, 0)
                    if sum == 2:
                        bulb.turn_on()
                        bulb.set_rgb(255, 0, 0)
                    if sum == 3:
                        bulb.turn_off()
            except Exception as e:
                time.sleep(10)
                bulb = yeelight.Bulb(IP)
                bulb.set_rgb(255, 255, 255)
                bulb.set_brightness(10)
                sums=5
                time.sleep(15)

            if sum == 1:
                cv2.putText(frame, '1', (150, 140), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), thickness=5)
                sums = sum
            if sum == 2:
                cv2.putText(frame, '2', (150, 140), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), thickness=5)
                sums = sum   
            if sum >= 3:
                cv2.putText(frame, '3', (150, 140), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), thickness=5)
                sums = sum
    if circles is None:
        sum = 0
        try:
            if sum != sums:
                    bulb = yeelight.Bulb(IP)
                    bulb.set_rgb(0, 0, 255)
        except Exception as e:
                time.sleep(10)
                bulb = yeelight.Bulb(IP)
                bulb.set_rgb(255, 255, 255)
                bulb.set_brightness(10)
                sums=5
                time.sleep(15)


        cv2.putText(frame, 'waiting', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), thickness=5)
        cv2.putText(frame, '0', (150, 140), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), thickness=5)
        sums = 0
    cv2.imshow('preview', frame)
    key = cv2.waitKey(10)
    if key == ord("q"):
        bulb.set_rgb(103,67,45)
        bulb.set_brightness(6)
        break

cv2.destroyAllWindows()
