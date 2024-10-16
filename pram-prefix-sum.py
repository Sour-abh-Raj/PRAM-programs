import concurrent.futures
import math

def prefix_sum(arr):
    n = len(arr)
    result = arr.copy()
    step = 1
    while step < n:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(step, n, 2 * step):
                futures.append(executor.submit(add, result, i, step))
            concurrent.futures.wait(futures)
        step *= 2
    result[-1] = 0
    step = n // 2
    while step > 0:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(step, n, 2 * step):
                futures.append(executor.submit(swap_add, result, i, step))
            concurrent.futures.wait(futures)
        step //= 2
    return result

def add(arr, i, step):
    arr[i] += arr[i - step]

def swap_add(arr, i, step):
    temp = arr[i]
    arr[i] += arr[i - step]
    arr[i - step] = temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("Original Array:", arr)
    result = prefix_sum(arr)
    print("Prefix Sum:", result)