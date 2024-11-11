#Reverse a string without using library functions.
str = "Hello World"
outputStr = ""
for i in range(len(str)):
    outputStr += str[len(str) - i - 1]

print(outputStr)