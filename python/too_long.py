def too_long(s):
    length = len(s)
    if length > 140:
        return True
    else:
        return False
    # Complete this function!
    # It should return True when s is longer than 140.
    # It should return False when s is shorter than 140.kgjg

# Test a short string
print("This should be False:")
print(too_long("I'm a short string!"))
print("This should be False:")
print(too_long("Im Mqueen!"))

# Test a long string
print("This should be True:")
print(too_long("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."))
print("This should be False:")
print(too_long("hello there we are testing anthor short string"))
