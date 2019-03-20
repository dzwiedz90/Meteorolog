import random
import os
import sys
import sleepTime


	
#Funkcja wypełniająca plik wygenerowanymi danymi
def generateData():
	dataFile = open('sensor1Data.txt', 'w')
	
	#Dane generowane w kolejości: prędkość wiatru, wilgotność powietrza, temperatura otoczenia, wysokość pokrywy śnieżnej, ciśnienie atmosferyczne
	wind = random.randrange(10, 70)    #prędkość wiatru
	humidity = random.randrange(10, 99)   #wilgotność powietrza
	temperature = random.uniform(-50.0, -10.0) #temperatura otoczenia
	snow = random.randrange(100, 400)   #wysokość pokrywy śnieżnej
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

generateData()
data = [line.strip() for line in open("sensor1Data.txt", 'r')]
data[0] = int(data[0])
data[1] = int(data[1])
data[2] = float(data[2][0:4])
data[3] = int(data[3])
data[4] = int(data[4])


	
#Generuje prędkość wiatru
def checkWindVelocity():
	windWelocity = data[0]
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z wiatromierza  ########################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z wiatromierza         ########################')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(windWelocity)
	return windWelocity
	
#Generuje wilgotność powietrza
def checkAirHumidity():
	airHumidity = data[1]
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z wilgotnościomierza ###################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z wilgotnościomierza        ###################')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(airHumidity)
	return airHumidity
	
#Generuje temperaturę otoczenia
def checkTemperature():
	temperature = data[2]
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z termometru  ##########################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z termometru         ##########################')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(temperature)
	return temperature
	
#Generuje wysokość pokrywy śnieżnej
def checkSnowHeight():
	snowHeight = data[3]
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych miernika głębokości pokrywy śnieżnej ###')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z miernika głębokości pokrywy śnieżnej      ###')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(snowHeight)
	return snowHeight
	
#Generuje ciśnienie atmosferyczne
def checkAtmosphericPresseure():
	atmosphericPresseure = data[4]
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z barometru ############################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z barometru        ############################')
	sleepTime.timeToSleep(random.uniform(1, 2.5))
	print(atmosphericPresseure)
	return atmosphericPresseure

def downloadData():
	print(sleepTime.currentTime()+' ######### ROZPOCZĘCIE ODCZYTU DANYCH Z CZUJNIKA NR 1     #####################################')
	sleepTime.timeToSleep(3)
	wind = checkWindVelocity()
	humidity = checkAirHumidity()
	temperature = checkTemperature()
	snow = checkSnowHeight()
	presseure = checkAtmosphericPresseure()
	print(sleepTime.currentTime()+' ######### ZAKOŃCZONO POBIERANIE DANYCH Z CZUJNIKA NR 1    ####################################')
	sleepTime.lineBreak()
	return wind, humidity,temperature, snow, presseure