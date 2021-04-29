def first_repeated(c):
    hash = dict()
    c = list(c)
    for i in range(len(c)):
        if c[i] not in hash:
            hash[c[i]] = 1
        else:
            return c[i]
    return "No repeated Element"
a = input("Enter : ")
print(first_repeated(a))