# rename your python file to 'counter.py' and class to 'Counter' (case sensitive)

from counter import Counter

c = Counter()

assert hasattr(c, "count"), "Has no attribute 'count'"
assert hasattr(c, "tick"), "Has no method 'tick'"
assert hasattr(c, "reset"), "Has no method 'reset'"

assert c.count == 0, "Counter isn't initialized at 0"

c.tick()

assert c.count == 1, "Counter doesn't increment correctly from 0 to 1"

c.tick()

assert c.count == 2, "Counter doesn't increment correctly from 1 to 2"

c.reset()

assert c.count == 0, "Counter doesn't increment correctly from 2 to 3"

print("you passed the test")