from math import factorial as f, e
n = int(input("Enter the n value: "))
x = int(input("Enter the x value: "))
real_value =  e**x
print("The real result of e^{0} is {1}".format(x, real_value))
result = 1 + x
for i in range(2, n+1):
    result += (x**i / f(i))
print("The result of e^{0} with iterating {1} times in Maclaurin formula is {2}".format(x, n, result))
print("The difference is(Up to {} digits): {}".format(n, format(real_value-result, ".{}f".format(n))))
