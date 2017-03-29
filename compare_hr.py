# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:43:10 2017

@author: cemalper
"""

import csv
import matplotlib.pyplot as plt
import tcxparser
import time
import pandas


def load_csv_data(filename,*args):
    try:    
        data = pandas.DataFrame.from_csv(filename,sep=";") #using pandas dataframe    
    except KeyError:
        if len(data) != 0:
            print("Wrong key")
        else:
            print ("Empty file")
        return
    except IOError:
        print("No file found!")
        return
    

if __name__ == "__main__":    
    with open("workout_updates.csv",'r', encoding = 'utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter = ';')
        data_list = [rows for rows in data]
        data_list = data_list[1:]
        secs = [float(data_list_elem[3]) for data_list_elem in data_list]
        hr = [float(data_list_elem[8]) if data_list_elem[8]!='' else 0 for data_list_elem in data_list] # set no hr data to 0
            
        plt.figure()
        plt.plot(secs,hr)
    
    
    
    tcx = tcxparser.TCXParser('activity_1641049237.tcx')
    hede2 = tcx.time_values()
    hede2 = [elem.split("T")[1].split("Z")[0] for elem in hede2]
    hede3 = [time.strptime(elems.split(',')[0],'%H:%M:%S.%f') for elems in hede2]
    hede4 = [x.tm_sec+x.tm_min*60+x.tm_hour*3600 for x in hede3]
    hede4 = [x - hede4[0] for x in hede4]
    plt.plot(hede4,tcx.hr_values())
    plt.xlabel("Seconds [s]")
    plt.ylabel("Heart Rate [bpm]")
    plt.grid()
    plt.show()
