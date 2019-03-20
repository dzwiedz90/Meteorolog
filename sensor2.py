import random
import os
import sys
import sleepTime
import sensorDataGenerator


	
def downloadData():
	print(sleepTime.currentTime()+' ######### ROZPOCZĘCIE ODCZYTU DANYCH Z CZUJNIKA NR 2     #####################################')
	sleepTime.timeToSleep(3)
	wind = sensorDataGenerator.checkWindVelocity()
	humidity = sensorDataGenerator.checkAirHumidity()
	temperature = sensorDataGenerator.checkTemperature()
	snow = sensorDataGenerator.checkSnowHeight()
	presseure = sensorDataGenerator.checkAtmosphericPresseure()
	print(sleepTime.currentTime()+' ######### ZAKOŃCZONO POBIERANIE DANYCH Z CZUJNIKA NR 2    ####################################')
	sleepTime.lineBreak()
	return wind, humidity,temperature, snow, presseure