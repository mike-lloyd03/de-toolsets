from filterTDMS import filter_and_interpolate_data
import os

print('Running batch filter...')
file_list = [file_name for file_name in os.listdir('./') if file_name[-4:] == 'tdms']

for file in file_list:
    filter_and_interpolate_data(file)

print("Batch process done")
