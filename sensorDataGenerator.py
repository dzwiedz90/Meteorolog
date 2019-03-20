import random
import os
import sys
import sleepTime



#Generuje prędkość wiatru
def checkWindVelocity():
	windWelocity = random.randrange(10, 70)
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z wiatromierza  ########################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z wiatromierza         ########################')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(windWelocity)
	return windWelocity
	
#Generuje wilgotność powietrza
def checkAirHumidity():
	airHumidity = random.randrange(10, 99)
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z wilgotnościomierza ###################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z wilgotnościomierza        ###################')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(airHumidity)
	return airHumidity
	
#Generuje temperaturę otoczenia
def checkTemperature():
	temperature = round(random.uniform(-50.0, -10.0), 1)
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z termometru  ##########################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z termometru         ##########################')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(temperature)
	return temperature
	
#Generuje wysokość pokrywy śnieżnej
def checkSnowHeight():
	snowHeight = random.randrange(100, 400)
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych miernika głębokości pokrywy śnieżnej ###')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z miernika głębokości pokrywy śnieżnej      ###')
	sleepTime.timeToSleep(random.uniform(1,2.5))
	print(snowHeight)
	return snowHeight
	
#Generuje ciśnienie atmosferyczne
def checkAtmosphericPresseure():
	atmosphericPresseure = random.randrange(850, 1100)
	print(sleepTime.currentTime()+' ######### Odczyt danych z czujnika, pobieranie danych z barometru ############################')
	sleepTime.timeToSleep(random.randrange(2,5))
	print(sleepTime.currentTime()+' ######### Połączono z czujnikiem, pobrano dane z barometru        ############################')
	sleepTime.timeToSleep(random.uniform(1, 2.5))
	print(atmosphericPresseure)
	return atmosphericPresseure