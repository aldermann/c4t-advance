import factorial

assert hasattr(
    factorial, "factorial"), "The function 'factorial' is not implemented. check if your function is named 'factorial'"

factorialFunc = factorial.factorial

assert factorialFunc(0) == 1, "Wrong base case"

f = 1

for i in range(1, 12):
    f *= i
    assert factorialFunc(i) == f, "Wrong answer"

print("you have passed the test")