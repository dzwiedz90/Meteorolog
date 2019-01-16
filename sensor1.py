import random
import os
import sys

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
	windWelocity = random.randrange(0, 70)
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z wiatromierza  ########################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z wiatromierza         ########################')
	sleep(random.uniform(1,2.5))
	print(windWelocity)
	return windWelocity
	
#Generuje wilgotność powietrza
def checkAirHumidity():
	airHumidity = random.randrange(0, 100)
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z wilgotnościomierza ###################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z wilgotnościomierza        ###################')
	sleep(random.uniform(1,2.5))
	print(airHumidity)
	return airHumidity
	
#Generuje temperaturę otoczenia
def checkTemperature():
	temperature = round(random.uniform(-50.0, 4.0), 1)
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z termometru  ##########################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z termometru         ##########################')
	sleep(random.uniform(1,2.5))
	print(temperature)
	return temperature
	
#Generuje wysokość pokrywy śnieżnej
def checkSnowHeight():
	snowHeight = random.randrange(0, 400)
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych miernika głębokości pokrywy śnieżnej ###')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z miernika głębokości pokrywy śnieżnej      ###')
	sleep(random.uniform(1,2.5))
	print(snowHeight)
	return snowHeight
	
#Generuje ciśnienie atmosferyczne
def checkAtmosphericPresseure():
	atmosphericPresseure = random.randrange(850, 1100)
	print(time()+' ######### Odczyt danych z czujnika, pobieranie danych z barometru ############################')
	sleep(random.randrange(2,5))
	print(time()+' ######### Połączono z czujnikiem, pobrano dane z barometru        ############################')
	sleep(random.uniform(1, 2.5))
	print(atmosphericPresseure)
	return atmosphericPresseure

def downloadData():
	print(time()+' ######### ROZPOCZĘCIE ODCZYTU DANYCH Z CZUJNIKA NR 1     #####################################')
	sleep(3)
	wind = checkWindVelocity()
	humidity = checkAirHumidity()
	temperature = checkTemperature()
	snow = checkSnowHeight()
	presseure = checkAtmosphericPresseure()
	print(time()+' ######### ZAKOŃCZONO POBIERANIE DANYCH Z CZUJNIKA NR 1    ####################################')
	return wind, humidity,temperature, snow, presseure