import re

target_string = "Jessa loves Python and pandas"
# Match six-letter word
pattern = r"\w{6}"

# match() method
result = re.match(pattern, target_string)
print(result)
# Output None

# search() method
result = re.search(pattern, target_string)
print(result.group()) 
# Output 'Python'

# findall() method
result = re.findall(pattern, target_string)
print(result) 
# Output ['Python', 'pandas'] 
