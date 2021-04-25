li = []
n = int(input("Enter the number of elements: "))
for i in range(1, n+1):
    elem = int(input("Enter the elements: "))
    li.append(elem)
li.sort()

print("The second smallest value of this list: ",li[1])