def calcSum(list):
    sum  = 0
    for i in list:
        sum = sum + list[i-1]
    return sum


def calcProduct(list):
    product = 1
    for i in list:
        product = product * list[i-1]
    return product



def main():
    print("Please enter a list of numbers")
    string = [int(i) for i in input().split()]
    print("The sum is " + str(calcSum(string)))
    print("The product is " + str(calcProduct(string)))
    return 0