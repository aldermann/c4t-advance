import power
import random

assert hasattr(power, "power"), "The function 'power' is not implemented. Check if your function is named 'power'"

powerFunc = power.power

assert powerFunc(100, 0) == 1, "Wrong answer"

for i in range(100):
    a, n = random.randint(1, 5), random.randint(1, 10)
    assert(powerFunc(a, n) == a ** n), "Wrong answer"

print("you passed the test")