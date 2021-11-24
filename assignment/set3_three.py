import re

n = "my number is 9544196592"
x = '[0-9]{10}'
match = re.findall(x,n)
print(match)
