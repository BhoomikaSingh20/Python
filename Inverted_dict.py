#program 12: define function to display histogram taking list of integers as input 

from matplotlib import pyplot as plt

def histogram_from_list(x):
    plt.hist(x, 10)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Histogram of user-entered list")
    plt.show()

ch = 'y'
while(ch=='y' or ch=='Y'):
    size = int(input("\nEnter size of list of integers: "))
    lst = []
    for i in range(1, size+1):
        x = int(input(" Enter Element: "))
        lst.append(x)
        
    histogram_from_list(lst)

    ch = input("\nWant to continue?(Y/N): ")
