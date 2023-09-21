#write a python code to to print a string ordered by the number of times each character appears in the string
#input: "hello world"
#output: "llohe wordl"

def sort_string(string):
    string = string.replace(" ", "")
    string = string.lower()
    string = list(string)
    string.sort()
    string = "".join(string)
    return string

# write 5 diffent test case to test above function

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

