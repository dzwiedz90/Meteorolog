import random
import os
import sys
import sleepTime
import sensorData


	
def downloadData():
	print(sleepTime.currentTime()+' ######### ROZPOCZĘCIE ODCZYTU DANYCH Z CZUJNIKA NR 3     #####################################')
	sleepTime.timeToSleep(3)
	wind = sensorData.checkWindVelocity()
	humidity = sensorData.checkAirHumidity()
	temperature = sensorData.checkTemperature()
	snow = sensorData.checkSnowHeight()
	presseure = sensorData.checkAtmosphericPresseure()
	print(sleepTime.currentTime()+' ######### ZAKOŃCZONO POBIERANIE DANYCH Z CZUJNIKA NR 3    ####################################')
	sleepTime.lineBreak()
	return wind, humidity,temperature, snow, presseure