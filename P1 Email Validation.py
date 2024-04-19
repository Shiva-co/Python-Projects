#Project 1 : Email Validation using String Functions

email = input(" Enter your Email : ")

k,j,d=0,0,0

if len(email) >= 6: # to check length of email
    if email[0].isalpha():   # check 1st letter is alphabet or not
        if ("@" in email) and (email.count("@")==1):  # if email contains @ sign and its count
            if (email[-4]==".") ^ (email[-3]=="."):   # to check whether . is in right position
                for i in email:
                    if i==i.isspace():              #if there is any space present
                        k=1
                    elif i.isalpha():
                        if i==i.upper():            # if there presets any upper case letter
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d==1
                if k==1 or j==1 or d==1:
                    print(" wrong email 5")
                else:
                    print(" Right Email ")
            else:
                print(" wrong email 4")
        else:
            print(" wrong email 3")
    else:
        print(" wrong email 2")
else:
    print(" wrong email 1 ")
