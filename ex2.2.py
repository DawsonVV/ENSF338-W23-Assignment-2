import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
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
        time_array_original.append(timeit.timeit(lambda: func1(data[i], 0, len(data[i]) - 1), number=1))
        x_values.append(len(data[i]))

    plt.plot(x_values, time_array_original, label="Original")
    plt.xlabel('Array Size')
    plt.ylabel('Time')
    plt.title('Time Complexity')
    plt.legend()
    plt.show()
        

        