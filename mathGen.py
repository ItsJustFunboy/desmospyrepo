import math

maxPowerOfX = 45
valuesOfX = 20

def mathFunctUsed(num):
    return math.cos(num)

for i in range(1, valuesOfX):
    print(str(i)+","+str(mathFunctUsed(i)))

# Equation

for j in range(1, maxPowerOfX):
    print("a_{"+str(j)+"}x_{1}^{"+str(j)+"}+", end="")
