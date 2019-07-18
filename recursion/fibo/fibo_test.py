import fibo

assert hasattr(fibo, "fibo"), "The function 'fibo' is not implemented. check if your function is named 'fibo'"

f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

fiboFunc = fibo.fibo

for id in range(len(f)):
    assert fiboFunc(id) == f[id], "Wrong answer"

print ("You've passed the test")
