import sys
import json
import timeit
import numpy as np
import matplotlib.pyplot as plt


sys.setrecursionlimit(20000)

def func2(array, start, end):
    
    p = array[(end + start)//2]
    low = start - 1
    high = end + 1
    while True:
        low +=1
        while array[low] < p:
            low += 1
        
        high -= 1
        while array[high] > p:
            high -= 1
            
        if(low >= high):
            return high

        array[low], array[high] = array[high], array[low]

def func1(array, low, high):
    if low < high:
        mid = func2(array, low, high)
        func1(array, low, mid)
        func1(array, mid + 1, high)
   

def main(): 
    time_array = []
    scale_x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    # Sort the arrays and put them in a file. That'll be later used to graph a plot. 
    with open('ex2.json','r') as iF:
        array = json.load(iF)
    for arr in array:
        func1(arr, 0, len(arr) - 1)
    sorted_array = array

    with open("ex2.5.json", "w") as outfile:
        json.dump(sorted_array, outfile) 

    array = json.load(open('ex2.json'))
    


    # We've edited the array elements, and now we try sorting it again. 
    # We'll time it and plot it.
    for arr in array:
        time_array.append(timeit.timeit(lambda : func1(arr,0,len(arr) - 1), number=1))
    
    plt.xticks(scale_x)
    plt.plot(scale_x, time_array, label = "After Changed Array Elements")
    plt.ylabel("Time (Seconds)")
    plt.xlabel("Array Length")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

