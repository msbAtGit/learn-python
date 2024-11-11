#Given a array of string return the String 
# which has the maximum length. 
# arr = ["Ram", "Abraham", "Peter"] 
# output is Abraham

arr = ["Ram", "Abraham", "Peter"]
maxStr = arr[0]
for i in range(len(arr)):
    if len(arr[i]) > len(maxStr):
        maxStr = arr[i]

print(maxStr)