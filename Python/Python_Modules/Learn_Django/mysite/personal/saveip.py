from datetime import datetime


def saveip(ip, routable):
    with open("/home/pi/Desktop/connections.txt", "a") as file:
        file.write("%s ::\t%s\t::\t%r\n" %(datetime.now(), ip, routable))
