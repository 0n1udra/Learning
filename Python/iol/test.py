import threading as th
def t1():
	while True:
		print("hi")

def t2():
	while True: print("BYE")

th1 = th.Thread(target=t1)
th2 = th.Thread(target=t2)
th1.start()
th2.start()
th1.join()
th2.join()
