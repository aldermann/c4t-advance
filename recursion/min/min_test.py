import min as minPackage
import random

assert hasattr(minPackage, "min"), "The function 'min' is not implemented. Check if your function is named 'min'"

minFunc = minPackage.min

test1 = [1, 3, 4, 5, 7, 9, 10]
test2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test4 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
test5 = [1]
test6 = [-1, 2, -3, -4, -5, - 6, 7, 8 , 9, 10]

random.seed()

test7 = [None] * 10

for i in range(10):
    test7[i] = random.randrange(-100, 10)



assert minFunc(test1) == min(test1), "Wrong answer"
assert minFunc(test2) == min(test2), "Wrong answer"
assert minFunc(test3) == min(test3), "Wrong answer"
assert minFunc(test4) == min(test4), "Wrong answer"
assert minFunc(test5) == min(test5), "Wrong answer"
assert minFunc(test6) == min(test6), "Wrong answer"
assert minFunc(test7) == min(test7), "Wrong answer"

print("you passed the test")