import random
import os
import sys

def time():
	import time
	wait = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	return wait

def sleep(timeSleep):
	import time
	time.sleep(timeSleep)
	
#Funkcja wypełniająca plik wygenerowanymi danymi
def generateData():
	dataFile = open('sensor2Data.txt', 'w')
	
	#Dane generowane w kolejości: prędkość wiatru, wilgotność powietrza, temperatura otoczenia, wysokość pokrywy śnieżnej, ciśnienie atmosferyczne
	wind = random.randrange(0, 70)    #prędkość wiatru
	humidity = random.randrange(0, 100)   #wilgotność powietrza
	temperature = random.uniform(-50.0, 4.0) #temperatura otoczenia
	snow = random.randrange(0, 400)   #wysokość pokrywy śnieżnej
	presseure = random.randrange(850, 1100)#ciśnienie atmosferyczne
	dataFile.write(str(wind))
	dataFile.write('\n')
	dataFile.write(str(humidity))
	dataFile.write('\n')
	dataFile.write(str(temperature))
	dataFile.write('\n')
	dataFile.write(str(snow))
	dataFile.write('\n')
	dataFile.write(str(presseure))
	dataFile.close()

data = [line.strip() for line in open("sensor2Data.txt", 'r')]
data[0] = int(data[0])
data[1] = int(data[1])
data[2] = float(data[2][0:5])
data[3] = int(data[3])
data[4] = int(data[4])


#Genereuje obecny czas
def time():
	import time
	wait = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	return wait

#Zatrzymuje wykonanie programu na timeSleep czasu
def sleep(timeSleep):
	import time
	time.sleep(timeSleep)
	
#Generuje prędkość wiatru
def checkWindVelocity():
	windWelocity = data[0]
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z wiatromierza  ########################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z wiatromierza         ########################')
	sleep(random.uniform(1,2.5))
	print(windWelocity)
	return windWelocity
	
#Generuje wilgotność powietrza
def checkAirHumidity():
	airHumidity = data[1]
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z wilgotnościomierza ###################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z wilgotnościomierza        ###################')
	sleep(random.uniform(1,2.5))
	print(airHumidity)
	return airHumidity
	
#Generuje temperaturę otoczenia
def checkTemperature():
	temperature = data[2]
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z termometru  ##########################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z termometru         ##########################')
	sleep(random.uniform(1,2.5))
	print(temperature)
	return temperature
	
#Generuje wysokość pokrywy śnieżnej
def checkSnowHeight():
	snowHeight = data[3]
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych miernika głębokości pokrywy śnieżnej ###')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z miernika głębokości pokrywy śnieżnej      ###')
	sleep(random.uniform(1,2.5))
	print(snowHeight)
	return snowHeight
	
#Generuje ciśnienie atmosferyczne
def checkAtmosphericPresseure():
	atmosphericPresseure = data[4]
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z barometru ############################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z barometru        ############################')
	sleep(random.uniform(1, 2.5))
	print(atmosphericPresseure)
	return atmosphericPresseure

def downloadData():
	generateData()
	print(time()+' ######### ROZPOCZĘCIE ODCZYTU DANYCH Z CZUJNIKA NR 2     #####################################')
	sleep(3)
	wind = checkWindVelocity()
	humidity = checkAirHumidity()
	temperature = checkTemperature()
	snow = checkSnowHeight()
	presseure = checkAtmosphericPresseure()
	print(time()+' ######### ZAKOŃCZONO POBIERANIE DANYCH Z CZUJNIKA NR 2    ####################################')
	return wind, humidity,temperature, snow, presseure