# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:43:10 2017

@author: cemalper
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import tcxparser
import time
import pandas as pd
import imp
import numpy as np
imp.reload(tcxparser)

def load_csv_data_frame(filename,*args):
    '''Reads the csv file exported from your app and creates a dataframe with corresponding header names.'''
    try:    
        data = pd.DataFrame.from_csv(filename,sep=";") #using pandas dataframe    
    except KeyError:
        if len(data) != 0:
            print("Wrong key")
        else:
            print ("Empty file")
        return
    except IOError:
        print("No file found!")
        return
    
def load_csv_data(filename,*args): 
    '''To be replaced by load_csv_data_frame'''
    with open(filename,'r', encoding = 'utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter = ';')
        data_list = [rows for rows in data]
    data_list = data_list[1:]
    secs = [float(data_list_elem[3]) for data_list_elem in data_list]
    hr = [float(data_list_elem[8]) if data_list_elem[8]!='' else 0 for data_list_elem in data_list] # set no hr data to 0
    plt.figure()
    plt.plot(secs,hr)
    return

def load_tcx(filename,*args):
    '''Loads the tcx and compiles the data into a dataframe'''
    tcx = tcxparser.TCXParser(filename)
    time_vals = tcx.time_values()
    dist = tcx.distance_points()
    temp = [elem.split("T")[1].split("Z")[0] for elem in time_vals]
    temp = [time.strptime(elems.split(',')[0],'%H:%M:%S.%f') for elems in temp]
    secs = [x.tm_sec+x.tm_min*60+x.tm_hour*3600 for x in temp]
    secs = [x - secs[0] for x in secs]
    dct_for_df = {"Seconds [s]" : secs, 
                  "Distance [m]" : dist, 
                  "Heart Rate [bpm]" : tcx.hr_values(), 
                  "Run Cadence" : tcx.run_cadence_points()}
    df = pd.DataFrame(dct_for_df)
    return df
    
def get_meter_per_beat(secs, hr, distance):
    pass

def plot_quantities(df,first,second,which_plot = 'plot'):
    '''Plots the two given quantities in a simple xy-plot'''
    tick_spacing = 100
    fig, ax = plt.subplots(1,1)
    if which_plot == 'plot':
        ax.plot(df[first],df[second])
    elif which_plot == 'scatter':
        ax.scatter(df[first],df[second])
    ax.xaxis.set_major_locator(ticker.LinearLocator(25))
    plt.xlim([0, max(df[first])])
    plt.xlabel(first)
    plt.ylabel(second)
    plt.grid()
    plt.show()
    
if __name__ == "__main__":   
    pass     

