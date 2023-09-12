def calcSum(list):
    sum  = 0
    for i in list:
        sum = sum + list[i-1]
    return sum

print(calcSum([1, 2, 3, 4, 5]))


def calcProduct(list):
    product = 1
    for i in list:
        product = product * list[i-1]
    return product

print(calcProduct([1,2,3,4]))