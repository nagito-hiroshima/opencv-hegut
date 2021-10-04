import requests
import datetime


def geturls(sum,mode):
    today = datetime.date.today().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    get = 'https://script.google.com/macros/s/AKfycbz9PoBi_Bs_P6aiI3D_cR3O1fU6JhGUu5J1ewF0R-VEwDNF65tm-7HJUze6qJOQoLMP/exec?p1='+str(today)+'&p2='+str(time)+'&p3='+str(mode)+'&p4='+str(sum)
    requests.get(get)

geturls(sum,"service")