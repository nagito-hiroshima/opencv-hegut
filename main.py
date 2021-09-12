import numpy as np
import cv2
import yeelight
import time

bulb = yeelight.Bulb("192.168.11.4")
bulb.turn_off()
bulb.set_rgb(255, 255, 255)
bulb.turn_on()
cap = cv2.VideoCapture(1)
sums =0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (33,33), 1)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 60, param1=10, param2=85, minRadius=20, maxRadius=80)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,0,255),2)
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            sum = (len(circles[0,:]))
            cv2.putText(frame, 'Lending Now', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), thickness=5)

            if sum != sums:
                bulb = yeelight.Bulb("192.168.11.4")
                if sum == 1:
                    bulb.set_rgb(255, 217, 0)
                if sum == 2:
                    bulb.set_rgb(255, 0, 0)
                    bulb.turn_on()
                    
                if sum == 3:
                    bulb.turn_off()



                

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
        if sum != sums:
                bulb = yeelight.Bulb("192.168.11.4")
                bulb.set_rgb(0, 0, 255)
                print("値が変更されました",sum)
        cv2.putText(frame, 'waiting', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), thickness=5)
        cv2.putText(frame, '0', (150, 140), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), thickness=5)
        sums = 0


    cv2.imshow('preview', frame) 
    key = cv2.waitKey(10)
    if key == ord("q"):
        break

cv2.destroyAllWindows()