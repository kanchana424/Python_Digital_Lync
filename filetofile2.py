f = open(r'C:\Users\kanchana\Desktop\input.txt','r')
content =f.readlines()
list1=[]
list2=[]
sum =0
for x in content:
	x=x.strip() # TO remove new line character
	str1=x.split("=") # Splitting the values with =
	list1=str1[-1] # To get the value after =
	if list1.isdigit()==True: # checking if the value is digit or not
		list2.append(list1)
	else:
		print("Variable doesn't hold a number")	

#print(list2)

for i in list2:  
	sum = sum + int(i) #Converting the string value in list to integer value
sum =str(sum) # To write into file the value must be string
f1 =open(r'C:\Users\kanchana\Desktop\output.txt','w')	
f1.write(sum)
#f1.close()
#f.close()
	








