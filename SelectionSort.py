#Implementing  Selection Sort



arr = [13, 89, 15, 28, 1, 7]

for i in range(0, len(arr) - 1):
    minIdx = i
    #finding the minimum index in the arr and swapping it
    for j in range(i + 1, len(arr)):
        if(arr[j] < arr[minIdx]):
            minIdx = j
        else:
            continue
    
    #Swapping value in ith index with the min index
    if(minIdx != i):
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)