arr = [8, 9, 10, 12, 9]
x = 12
i = int(0)
maxlen = len(arr) - 1
flag = False
for i in range(len(arr)):
    if arr[i] == x:
        flag = True

if flag:
    print("Element found")
else:
    print("Not found")

