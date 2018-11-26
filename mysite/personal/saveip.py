from datetime import datetime

def saveip(ip, routable):
    with open("/home/drake/connections.txt", "a") as file:
        file.write(f"{datetime.now()}\t{ip}\t{str(routable)[0]}\n")
