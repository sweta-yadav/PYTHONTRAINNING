
# Recursive Bubble Sort
def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort(arr, n - 1)

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    bubble_sort(arr)
    print(arr)
