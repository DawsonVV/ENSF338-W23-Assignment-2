import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1_changed(arr, low, high):
    if low < high:
        pi = func2_changed(arr, low, high)
        func1_changed(arr, low, pi-1)
        func1_changed(arr, pi + 1, high)
    

def func2_changed(array, start, end):
    index_t = (start + end) // 2
    array[start], array[index_t] = array[index_t], array[start]
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high




if __name__ == '__main__':

    time_array_original = []
    x_values = []

    time_array_changed = []
    x_values_changed = []

    with open('ex2.json', "r") as json_file:
        data = json.load(json_file)

    for i in range(len(data)):
        time_array_changed.append(timeit.timeit(lambda: func1_changed(data[i], 0, len(data[i]) - 1), number=1))
        x_values_changed.append(len(data[i]))

    plt.xlabel('Array Size')
    plt.ylabel('Time')
    plt.title('Time Complexity')
    plt.plot(x_values_changed, time_array_changed, label="Changed")


    plt.legend()
    plt.show()
        

        