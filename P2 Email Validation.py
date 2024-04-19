#Project 2 : Email Validation using Regex Module

# a-z
# 0-9
# . _ one time
# @ one time
# . in end position 2,3

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email = input(" Enter Your Email : ")

if re.search(email_condition,email):
    print(" Right Email ")
else:
    print(" Wrong Email ")
