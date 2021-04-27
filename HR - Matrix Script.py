import re
matrix = list()
for _ in range(int(input().split()[0])):
    matrix.append(list(input()))
matrix = list(zip(*matrix))
sample = str()
for subset in matrix:
    for letter in subset:
        sample += letter
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))