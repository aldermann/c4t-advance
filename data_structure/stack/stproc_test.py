from stproc import StringProcessor

proc = StringProcessor()

assert hasattr(proc, "__init__"), "there are attribute(s) unimplemented"
assert hasattr(proc, "stack"), "there are attribute(s) unimplemented"
assert hasattr(proc, "reverse"), "there are attribute(s) unimplemented"
assert hasattr(proc, "process_sequence"), "there are attribute(s) unimplemented"
assert hasattr(proc, "binary_string"), "there are attribute(s) unimplemented"
assert hasattr(proc, "is_balanced"), "there are attribute(s) unimplemented"

print("testing reverse method")
assert proc.reverse("abcdef") == "fedcba", "reverse method not working correctly"
assert proc.reverse("abccba") == "abccba", "reverse method not working correctly"

print("testing process_sequence method")
assert proc.process_sequence("ab*de*abcdef") == "adabcdef", "wrong answer"
assert proc.process_sequence("d*e*f*g*") == "", "wrong answer"
assert proc.process_sequence("d****ef") == "ef", "wrong answer"

print("testing binary_string method")
assert proc.binary_string(124) == "1111100", "wrong answer"
assert proc.binary_string(10) == "1010", "wrong answer"

print("testing is_balanced method")
assert proc.is_balanced("{{{}}}"), "wrong answer"
assert not proc.is_balanced("{{{}"), "wrong answer"
assert not proc.is_balanced("}}{{"), "wrong answer"
assert proc.is_balanced("{{{}}{}{}}"), "wrong answer"

print("you passed the test")
