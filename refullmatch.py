import re

# string length of 42
str1 = "My name is maximums and my salary is 1000$"
print("str1 length: ", len(str1))

result = re.fullmatch(r".{42}", str1)

# print entire match object
print(result)

# print actual match value
print("Match: ", result.group())
