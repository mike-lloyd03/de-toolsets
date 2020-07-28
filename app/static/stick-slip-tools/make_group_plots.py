import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_group_plots(data_blocks, tdms_data, name=''):
    '''
    Generate a multi plot figure of the input list of dataframes
    
    Parameters:
    data_blocks (list): an iterable of ranges of data e.g. [[a1,a2],[b1,b2]]
    tdms_data (list): an iterable of dataframes with the data to be plotted
    name (str): optional, the name of the plot

    Returns:
    pyplot: A figure with the multiple sublots of data
    '''
    tdms_len = len(tdms_data)
    fig, axs = plt.subplots(tdms_len, figsize=[8, 6])
    fig.suptitle(name)
    fig.subplots_adjust(hspace=1)
    fig.subplots_adjust(wspace=0.0)
    for i in range(tdms_len):
      plot_x = tdms_data[i]['Cycle Count']
      plot_y = tdms_data[i]['CoF']
      axs[i].plot(plot_x, plot_y)
      axs[i].axis([min(plot_x), max(plot_x), 0, 0.2])
      axs[i].set_title(f'{min(data_blocks[i])} to {max(data_blocks[i])} cycles')
      axs[i].set_xlabel('Cycles')
      axs[i].set_ylabel('CoF')
    return plt
