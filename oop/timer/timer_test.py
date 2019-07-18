from timer import Timer

t = Timer()

assert hasattr(t, "seconds"), "Missing method or attribute. Check the class diagram."
assert hasattr(t, "minutes"), "Missing method or attribute. Check the class diagram."
assert hasattr(t, "hours"), "Missing method or attribute. Check the class diagram."
assert hasattr(t, "tick"), "Missing method or attribute. Check the class diagram."
assert hasattr(t, "reset"), "Missing method or attribute. Check the class diagram."

assert t.seconds == 0, "Counter is not initialized correctly"
assert t.minutes == 0, "Counter is not initialized correctly"
assert t.hours == 0, "Counter is not initialized correctly"

for _ in range(100):
    t.tick()

assert t.seconds == 40, "Counter does not count correctly"
assert t.minutes == 1, "Counter does not count correctly"
assert t.hours == 0, "Counter does not count correctly"

t.reset()

assert t.seconds == 0, "Counter does not reset correctly"
assert t.minutes == 0, "Counter does not reset correctly"
assert t.hours == 0, "Counter does not reset correctly"

for _ in range(3661):
    t.tick()

assert t.seconds == 1, "Counter does not count correctly"
assert t.minutes == 1, "Counter does not count correctly"
assert t.hours == 1, "Counter does not count correctly"

t.hours = 23
t.minutes = 59
t.seconds = 59

t.tick()

assert t.seconds == 0, "Counter does not count correctly"
assert t.minutes == 0, "Counter does not count correctly"
assert t.hours == 0, "Counter does not count correctly"

print("you pass the test")


