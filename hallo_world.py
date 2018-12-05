# -*- coding: utf-8 -*-
"""
Created on Wed Dec 05 17:44:06 2018

@author: Mordi Hotoveli
"""

import numpy as np
import matplotlib.pyplot as plt

startTime = 0
stopTime = 100
timestep = 0.001

def hello():
    
    a = '\nhello world'
    print (a)

def main():
    hello()
    
    step = np.arange(startTime, stopTime, timestep, dtype=np.float)
    h = np.arange(startTime, stopTime, timestep, dtype=np.float)
    for n in step:
       #i +=1 
       h[n] = np.sin(n)
       #print(h)
       
    fig, ax = plt.subplots(1, 1)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('voltage')
    ax.set_title('sin(wt)')
    ax.grid(True)
    #ax.set_savefig(step,h,"test.png")
    ax.plot(h)
    ax.set_ylim(-1, 1)
    ax.set_xlim(startTime, stopTime)
    #ax.show()

if (__name__ == "__main__"):
    main()

