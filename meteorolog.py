#Program odczytujący dane z czujek meteorologicznych
import os
import sys
import time
import sensor1
import sensor2

print('##############################################################################################')
print('##################################                          ##################################')
print('##################################        METEOROLOG        ##################################')
print('##################################                          ##################################')
print('##############################################################################################')
print(' ')
print('ver. 1.0')
print('(C) by dzwiedz90\nWszystkie prawa zastrzeżone')
print(' ')

input('Wciśnij enter, aby kontynuować...')
os.system('cls')

choose = 0
while choose == 0:
	print('1. Odczytaj dane z czujek')
	print('2. Wyjdź')	
	choose = input('Wybierz tryb i naciśnij enter: ')
	os.system('cls')
	if choose == '1':
		break
	elif choose == '2':
		sys.exit(0)

sensor1Data = sensor1.downloadData()
print(sensor1Data)
sensor2Data = sensor2.downloadData()
print(sensor2Data)