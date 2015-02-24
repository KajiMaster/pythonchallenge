
message = ""
counter = 0
with open("code2.txt", "r") as content_file:
    code = content_file.read()

    while counter < len(code):
        
        if code[counter] == "[A-Z]" and code[counter + 1] == "[A-Z]" and code[counter + 2] == "[A-Z]" and code[counter + 3] == "[a-z]" and code[counter + 4] == "[A-Z]" and code[counter + 5] == "[A-Z]" and code[counter + 6] == "[A-Z]":
            message += code[counter + 3]
            counter += 1
        else:
            counter += 1
    
print message
    
