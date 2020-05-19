# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    index = 0
    swaps = 0
    last_element = len(arr) - 1
    while swapped:
        if index < last_element: 
            if arr[index] > arr[index + 1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
                swaps += 1
            index += 1
        else: 
            last_element -= 1
            if swaps == 0:
                swapped = False
            else:
                index = 0
                swaps = 0
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:
        return arr
    if maximum == -1:
        maximum = max(arr)
    buckets = [0 for _ in range(maximum+1)]
    for x in arr:
        if x < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        buckets[x] += 1
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j+=1
            buckets[i]-=1

    return arr
