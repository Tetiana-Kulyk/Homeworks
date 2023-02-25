import re
with open("text", "r") as f:
    content = f.read()
    print(content)
    print(re.split("\. | \.\.\.\. | \.\.\.\.\.\.", content))
