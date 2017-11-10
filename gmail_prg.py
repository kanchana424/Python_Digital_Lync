#Gmail project

username = "kanchana"
password = "kanchana"
count =0
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

