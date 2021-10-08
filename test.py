#pip install numpy
#pip install opencv-contrib-python
#pip install yeelight
#pip install requests


import numpy as np
import cv2
import yeelight
import time
import requests
import datetime

cap = cv2.VideoCapture(1)
sums =0

def geturls(sum,mode):
    today = datetime.date.today().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    get = 'https://script.google.com/macros/s/AKfycbz9PoBi_Bs_P6aiI3D_cR3O1fU6JhGUu5J1ewF0R-VEwDNF65tm-7HJUze6qJOQoLMP/exec?p1='+str(today)+'&p2='+str(time)+'&p3='+str(mode)+'&p4='+str(sum)
    requests.get(get)

try:
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
                        geturls(sum,"service")#service 運用中,Restart 再起動中,stop 停止中,other メンテナンス中
                except Exception as e:
                    sums=5
                    geturls(sum,"Restart")#service 運用中,Restart 再起動中,stop 停止中,other メンテナンス中

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
                    print(0)
            except Exception as e:
                    sums=5
                    time.sleep(15)
                    geturls(sum,"Restart")#service 運用中,Restart 再起動中,stop 停止中,other メンテナンス中


            cv2.putText(frame, 'waiting', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), thickness=5)
            cv2.putText(frame, '0', (150, 140), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), thickness=5)
            sums = 0
        cv2.imshow('preview', frame)
        key = cv2.waitKey(10)
        if key == ord("q"):
            geturls(sum,"stop")#service 運用中,Restart 再起動中,stop 停止中,other メンテナンス中
            break

    cv2.destroyAllWindows()
except Exception as e:
    geturls(sum,"other")#service 運用中,Restart 再起動中,stop 停止中,other メンテナンス中
