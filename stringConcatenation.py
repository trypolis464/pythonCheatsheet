# This demonstrates how to combine strings with other variables.

# Using +, like in C++ with std::string or C# with System.String
test = "World"
print("Hello, " + test + "!")

# You can also convert other variables to strings to print them. This is necessary when using +.
theNumber = 58
print("The number is " + str(theNumber))

# Using f, for format.
# Note that is't not necessary to do type conversions here.
gpa = 3.93
print(f"You ended with a GPA of {gpa}.")

# Using .format.
testStr = "Meow"
print("Cats say {}, {}, {}".format(testStr, testStr, testStr))
