#!/usr/bin/python

import string
letters = list(string.lowercase) + list(string.uppercase)
info = ""
code = open("code.txt","r")
for line in code:
    for character in line:
        for i in letters:
            if character == i:
                info += character
print "what you seek is:" + info
    
code.close()
