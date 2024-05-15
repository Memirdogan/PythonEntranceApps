import math

n = int(input("Fibonacci sayısını girin: "))

f = ((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5))

print("{:.2f}".format(f))
