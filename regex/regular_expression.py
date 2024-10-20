import re

pattern = input("Enter a regular expression: ")

match_count = 0

with open("mbox.txt", 'r') as file:
    for line in file:
        if re.search(pattern, line):
            match_count += 1

print(f"mbox.txt had {match_count} lines that matched {pattern}")