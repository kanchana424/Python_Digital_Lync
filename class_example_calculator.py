#Program written in class which has methods for add, mul,div and sub.

class calculator:
    def __init__(self):
        self.num1=int(input("Please a numerical value: \n"))
        self.num2=int(input("Please a numerical value: \n"))
    
    def choice(self):
        choice = input("0. To quit \n"
                          "1. For addition \n"
                          "2. For substraction \n"
                          "3. For divison \n"
                          "4. For multiplication \n"
                          "Please enter your choice of input: ")
        return choice
                     
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def div(self):
        return self.num1/self.num2

    def mul(self):
        return self.num1*self.num2
    
obj = calculator()
#val_choice =obj.choice()
val_choice ="1"
while val_choice!="0":
    val_choice =obj.choice() # If i remove this here and place it below calling the class, the output of add prints continuosuly why
    if val_choice =="1":   
        print(obj.add())   
    elif val_choice =="2":
        print(obj.sub())
    elif val_choice =="3":
        print(obj.div())
    elif val_choice =="4":
        print(obj.mul())
    elif val_choice ==0:
        print("You entered to quit the caluclator \n")
    else:
        print("You entered wrong choice \n")
        val_choice =obj.choice()



