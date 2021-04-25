# answer for unsolved2.py
li = []
n = int(input("Enter list size:"))


for i in range(n):
    a = int(input("Enter element:"))
    li.append(a)

for i in range(0, n, 2):
    if i+1 >= n:
        break
    temp = li[i]
    li[i] = li[i+1]
    li[i+1] = temp

print(li)