def calcSum(list):
    sum  = 0
    for i in list:
        sum = sum + list[i-1]
    return sum

print(calcSum([1, 2, 3, 4, 5]))