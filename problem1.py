def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

arr = [10, 20, 30, 40]
reverse_array(arr)
print(arr)
