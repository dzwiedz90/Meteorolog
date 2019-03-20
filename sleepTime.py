import time

#Genereuje obecny czas
def currentTime():
	wait = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	return wait

#Zatrzymuje wykonanie programu na timeSleep czasu
def timeToSleep(timeSleep):
	time.sleep(timeSleep)
	
def lineBreak():
	print(' ')
	print(' ')
	print(' ')