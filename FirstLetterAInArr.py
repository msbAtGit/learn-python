#In an array of string, return all the string which start with the letter 'a' 
# (Case insensitive) 
# for eg arr = ["apple", "Ali", "mango","Brush"] 
# it should print apple, Ali


arr = ["apple", "Ali", "mango","Brush"] 
outputStr = ""
for i in range(len(arr)):
    if arr[i][0] == 'a' or arr[i][0] == 'A':
        if outputStr == "":
            outputStr += arr[i]
        else:
            outputStr += ", " + arr[i]
        
    else:
        continue

print(outputStr)