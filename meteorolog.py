#Program odczytujący dane z czujek meteorologicznych
#Jeżeli dane nie wyświetlają się poprawnie w oknie należy powiększyć okno
import os
import sys
import time
import sensor1
import sensor2
import sensor3


def main():
	os.system('cls')
	print('##############################################################################################')
	print('##################################                          ##################################')
	print('##################################        METEOROLOG        ##################################')
	print('##################################                          ##################################')
	print('##############################################################################################')
	print(' ')
	print('ver. 1.2')
	print('(C) by dzwiedz90\nWszystkie prawa zastrzeżone')
	print(' ')
	print(' ')
	print(' ')
	print('*Jeżeli dane nie wyświetlają się poprawnie w oknie należy powiększyć okno*')
	print(' ')
	print(' ')
	print(' ')
	input('Wciśnij enter, aby kontynuować...')

	choose = 0
	while_exit = 'dupa'
	while while_exit == 'dupa':
		os.system('cls')
		print('##############################################################################################')
		print('##################################                          ##################################')
		print('##################################        METEOROLOG        ##################################')
		print('##################################                          ##################################')
		print('##############################################################################################')
		print(' ')
		print('ver. 1.2')
		print('(C) by dzwiedz90\nWszystkie prawa zastrzeżone')
		print(' ')
		print(' ')
		print('1. Odczytaj dane z czujek')
		print('2. Wyjdź')	
		choose = input('Wybierz tryb i naciśnij enter: ')
		os.system('cls')
		if choose == '1':
			break
		elif choose == '2':
			sys.exit(0)
		else:
			continue

	os.system('cls')
	sensor1Data = sensor1.downloadData()
	sensor2Data = sensor2.downloadData()
	sensor3Data = sensor3.downloadData()
	input('ZAKOŃCZONO POBIERANIE DANYCH Z SENSORÓW. WCIŚNIJ ENTER, ABY KONTYNUOWAĆ...')

	os.system('cls')
	print(' ')
	
	#1 do 2	     1 do 3	    	5 do 3	  	1 do 3		3 do 4
	#wind,       humidity,	  temperature, 	snow,     presseure
	print('+-------------------------------------------------------------------------------------------------------------------------+')
	print('|          ||  Prędkość wiatru  || Wilogtność powietrza || Temperatura || Głębokość pokrywy śniegu || Ciśnienie powietrza |')
	print('+----------||-------------------||----------------------||-------------||--------------------------||---------------------+')
	print('+----------||-------------------||----------------------||-------------||--------------------------||---------------------+')
	print('| Sensor 1 ||       ',sensor1Data[0],'        ||       ',sensor1Data[1],'           ||    ',sensor1Data[2],'  ||           ',sensor1Data[3],'          ||          ',sensor1Data[4],'      |')
	print('+----------||-------------------||----------------------||-------------||--------------------------||---------------------+')
	print('| Sensor 2 ||       ',sensor2Data[0],'        ||       ',sensor2Data[1],'           ||    ',sensor2Data[2],'  ||           ',sensor2Data[3],'          ||          ',sensor2Data[4],'      |')
	print('+----------||-------------------||----------------------||-------------||--------------------------||---------------------+')
	print('| Sensor 3 ||       ',sensor3Data[0],'        ||       ',sensor3Data[1],'           ||    ',sensor3Data[2],'  ||           ',sensor3Data[3],'          ||          ',sensor3Data[4],'      |')
	print('+----------||-------------------||----------------------||-------------||--------------------------||---------------------+')
	print('+-------------------------------------------------------------------------------------------------------------------------+')
	print(' ')
	print(' ')
	input('ZAKOŃCZENIE POBIERANIA WYNIKÓW. POWRÓT DO MENU GŁÓWNEGO WCISNIJ ENTER...')
	main()
	
	
main()