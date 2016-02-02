
import tkinter as tk
from tkinter import filedialog

print("Starting up...")
earth_temp = input('Input the average measured at the surface of the earth... ')
space_temp = input('Input the average measured in empty space... ')

earth_temp = float(earth_temp)
space_temp = float(space_temp)

assert earth_temp > space_temp

slope_correction = (300-3)/(earth_temp - space_temp)
intercept = 300 - (slope_correction * earth_temp)

print("\nThe data correction line is y = "+str(slope_correction)+"*x + "+str(intercept))
print("\nPlease select the .rad file with the data you want to graph")

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

print('\n'+file_path)

rad_file = open(file_path, 'r')
lines = rad_file.readlines()
rad_file.close()
line_data = lines[1].split(' ')

print(line_data)

starting_freq = float(line_data[12])
freq_step = float(line_data[13])
num_bins = float(line_data[17])

print('\n', starting_freq, freq_step, num_bins)

num_samples = len(lines) 

print('\nbeginning data separation...')

for sample_num in range(num_samples):
	lines[sample_num] = lines[sample_num].split(' ')
	
	for item in lines[sample_num]:
		if item == '':
			lines[sample_num].remove('')
		else:
			pass

print(lines[1])
print('\nbeginning bin averaging...')

average_powers = []
