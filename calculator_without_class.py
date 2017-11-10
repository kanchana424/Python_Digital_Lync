#Program written in class which has methods for add, mul,div and sub.
num1=int(input("Please a numerical value: \n"))
num2=int(input("Please a numerical value: \n"))
#val_choice =obj.choice()
val_choice ="1"
while val_choice!="0":
    val_choice =input("0. To quit \n"
                "1. For addition \n"
                "2. For substraction \n"
                "3. For divison \n"
                "4. For multiplication \n"
                "Please enter your choice of input: ")
    if val_choice =="1":   
        print(num1+num2)   
    elif val_choice =="2":
        print(num1-num2)
    elif val_choice =="3":
        print(num1/num2)
    elif val_choice =="4":
        print(num1*num2)
    elif val_choice ==0:
        print("You entered to quit the caluclator \n")
    else:
        print("You entered wrong choice \n")
        val_choice =input("0. To quit \n"
                "1. For addition \n"
                "2. For substraction \n"
                "3. For divison \n"
                "4. For multiplication \n"
                "Please enter your choice of input: ")



