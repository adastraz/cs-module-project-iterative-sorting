def linear_search(arr, target):
    # Your code here
    for x in range(len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target, right=None, left=0):
    if not right:
        right = len(arr)-1
    else:
        right = right
    print(right)
    try:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
            return binary_search(arr, target, right, left)
        elif arr[mid] > target:
            right = mid - 1
            return binary_search(arr, target, right, left)
    except IndexError:
        return -1