#Implement the bubble sort algorithm

#arr = [13, 89, 15, 28, 1, 7]

arr = ["Superman", "Batman", "supergirl", "Aquaman", "Wonder Woman"]
swapped = True
while swapped:
    swapped = False
    for j in range(0, len(arr) - 1):
        if(arr[j].lower() > arr[j+1].lower()):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    
print(arr)