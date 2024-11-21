# Insertion sort
# Assume an array is sorted starting from the 0th Index
# Run a loop from 1 to len(arr)
# Identify the location where the element has to be inserted
# Iterate till the end


arr = [8, 8, 7, 12, 8]
#for j = 2 to A.length
for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i = i - 1
        
    arr[i + 1] = key
        
print(arr)

   

    