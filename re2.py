# target_string = "Emma is a basketball player who was born on June 17, 1993"
import re

target_string = "Emma is a basketball player who was born on June 17"
result = re.match(r"\w{4}", target_string) #

# printing the Match object
print("Match object: ", result)
# Output re.Match object; span=(0, 4), match='Emma'

# Extract match value
print("Match value: ", result.group())
# Output 'Emma'
