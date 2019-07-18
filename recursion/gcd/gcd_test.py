import gcd

assert hasattr(gcd, "gcd"), "The function 'gcd' is not implemented. check if your function is named 'gcd'"

gcdFunc = gcd.gcd

assert gcdFunc(100, 25) == 25, "Wrong answer"
assert gcdFunc(21, 7) == 7, "Wrong answer"
assert gcdFunc(6, 9) == 3, "Wrong answer"
assert gcdFunc(10000, 200) == 200, "Wrong answer"
assert gcdFunc(90, 89) == 1, "Wrong answer"
assert gcdFunc(99, 33) == 33, "Wrong answer"
assert gcdFunc(10000, 1) == 1, "Wrong answer"
assert gcdFunc(12, 15) == 3, "Wrong answer"
assert gcdFunc(20, 20) == 20, "Wrong answer"
assert gcdFunc(35, 7) == 7, "Wrong answer"
assert gcdFunc(1, 1) == 1, "Wrong answer"

print("you have passed the test")