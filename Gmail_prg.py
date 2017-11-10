#Gmail project

username = "kanchana"
password = "kanchana"
count =0
'''
while True:
    user = input("Enter username:")
    if user == username:
        print("Your username is correct")
        break
while count <3:
    pw = input("Please enter your password:")
    if pw == password:
        print("Success you can access your mail")
        break
    else:
        count = count +1
        print('Sorry you entered wrong password')
'''
user = input("Enter username:")
while True:
    # count=0
    if user == username:
        print("Your username is correct")
        # continue
        pw = input("Please enter your password:")
        if(count<3):

            if pw == password :
                print("Success you can access your mail")
                break
            else:
                count = count +1
                print('Sorry you entered wrong password',count)
        else:
            break
    else:
        user = input("Enter username:")


