#program 26: a function to plot a graph of people with pulse rate p vs. height h

from matplotlib import pyplot as plt
import numpy as np

def pulse_height(p, h):
    plt.xlabel("x axis: Pulse Rate(in bmp)")
    plt.ylabel("y axis: Height(in cm)")
    plt.title("Pulse vs Height Graph")
    plt.plot(p,h)
    plt.show()

ch = 'y'
while(ch=='y' or ch=='Y'):
    size = int(input("/nEnter size of data: "))
    p = []
    h = []
    for i in range(size):
        pulse_rate = float(input("/nEnter Pulse rate(bpm): "))
        p.append(pulse_rate)
        height = float(input("Enter height(in cm): "))
        h.append(height)
        print()

    pulse_height(p,h)

    ch = input("Want to continue?(y/n): ")
