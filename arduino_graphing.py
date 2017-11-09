import serial
from drawnow import *
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import csv

arduino = serial.Serial('COM3', 9600)
beer_temps = []
fridge_temps = []
hours = []

plt.ion()


def makeFig():
	plt.ylim(0, 35)
	plt.title('Fermentation temperatures live')
	plt.grid(True, which='both')
	plt.ylabel('Beer temperature (°C)')
	plt.plot(beer_temps, 'ro-', label = 'Beer temp °C')
	plt.legend(loc='upper left')
	plt2=plt.twinx()
	plt.ylim(0,35)
	plt.ylabel('Fridge (Ambient) temperature (°C)')
	plt2.plot(fridge_temps, 'b^-', label = 'Fridge temp °C')
	plt2.legend(loc='upper right')



def draw_graph():
	count = 0
	while True:
		while (arduino.inWaiting()==0): #waits until there is data
			pass
		temps_data = arduino.readline().decode("utf-8").split(" , ")
		bt = float(temps_data[0])
		ft = float(temps_data[1])

		beer_temps.append(bt)
		fridge_temps.append(ft)

		drawnow(makeFig)
		plt.pause(.000001)
		count += 1
		hours.append(count)
		if count>=72:
			beer_temps.pop(0)
			fridge_temps.pop(0)

			if count%24==0:
				logs = zip(beer_temps, fridge_temps, hours)
				with open('{}.csv'.format(date.today()), 'w') as csvfile:
					wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
					wr.writerow(logs)



draw_graph()
