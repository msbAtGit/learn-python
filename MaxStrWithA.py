# Given an array of strings
# return the array which has the maximum
# occurence of a in it.

def numberOccurenceOfA(str):
    count = 0
    for i in range(0, len(str)):
        if(str[i] == 'a' or str[i] == 'A'):
            count += 1
    
    return count

def maxAsInStr(arr):
    if arr is None or len(arr) == 0:
        return ""
    maxAsStr = arr[0]
    maxCount = numberOccurenceOfA(arr[0])
    for i in range(1, len(arr)):
        currCount = numberOccurenceOfA(arr[i])
        if(maxCount < currCount):
            maxAsStr = arr[i]
            maxCount = currCount

    return maxAsStr


print(maxAsInStr(["apple", "orange", "algae", "characterization"]))
