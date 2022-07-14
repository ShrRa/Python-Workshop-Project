from functools import reduce

def product(a, b):
    return a * b

l = [1, 2, 3]

print(reduce(product, l))
print(reduce((lambda a, b: a * b), l))

def sum_of_squares(arr):
    arr=[int(i)*int(i) for i in arr if not str(i).startswith('#')]
    return reduce(lambda x, y: x + y, arr)

print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))

print(sum_of_squares(['1', '2', '#100', '3']))
