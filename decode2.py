import re

message = ""
sort = ""
used = []
with open("fake.txt", "r") as content_file:
    code = content_file.read()
  
    for match in re.findall('[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]', code):
        message += match[3]

for i in message:
    if i not in used:
        used.append(i)
        sort += i

print sort
        


