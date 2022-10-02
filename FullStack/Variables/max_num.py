def find_max(arr):
    max = arr[0]
   
    for x in arr:
        if x > max:
            max = x
   
    return max    
        

array = [23, 56, 78,34, 32, 10, 3, 6, 45]

print(find_max(array))