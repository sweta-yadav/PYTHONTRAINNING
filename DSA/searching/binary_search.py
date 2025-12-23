
# Recursive Binary Search (Array must be sorted)
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print("Index:", binary_search(arr, 7, 0, len(arr)-1))
