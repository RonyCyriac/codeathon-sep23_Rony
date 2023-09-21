# Test Case 1
assert sort_string("hello world") == "dehllloorw"

# Test Case 2
assert sort_string("Python is awesome") == "aeehimoopstwythns"

# Test Case 3
assert sort_string("The quick brown fox jumps over the lazy dog") == "abbbccddddeeeeeffggghhhiijjkklllmnoooopqrrrrssttuuvwxyz"

# Test Case 4
assert sort_string("1234567890") == "0123456789"

# Test Case 5
assert sort_string("") == ""