def rotate_array(arr):
    if len(arr) == 0:
        return arr
    
    
    return [arr[-1]] + arr[:-1]


arr = [1, 2, 3, 4, 5]
rotated = rotate_array(arr)
print(rotated)
