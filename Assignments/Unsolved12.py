def remove_ele(c,n):
    if n < len(c) and n > 0:
        return c[:n] + c[n+1:]
    else:
        return "Invalid index"
a = input("Enter string")
b = int(input("Enter index to be deleted"))

print(remove_ele(a,b))