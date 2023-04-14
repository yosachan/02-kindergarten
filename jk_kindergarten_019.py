values = ['A', 'B', 'C', 'D']
print(values)
# values.insert(0, 999)
# print(values)
# values.insert(5, 999)
# print(values)
# values[1] = 'abc'
# print(values)
del values[1]
print(values)

cases = [100, 200, 300, 400, 500, 600, 700]
index = 0
total = 0
len_cases = len(cases)
while index < len_cases:
    total = total + cases[index]
    index = index + 1
    print(total)
print(len_cases)
print(total)

values = [1, 2, 3, 4]
for value in values:
    print(value, value * value)

cases = [100, 200, 300, 400, 500, 600, 700]
total = 0
for case in cases:
    total = total + case
    print(total)
print(total)