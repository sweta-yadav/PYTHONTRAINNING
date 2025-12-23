
# Recursive Linear Search
def linear_search(arr, target, index=0):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search(arr, target, index + 1)

if __name__ == "__main__":
    arr = [4, 7, 1, 9, 3]
    print("Index:", linear_search(arr, 9))
