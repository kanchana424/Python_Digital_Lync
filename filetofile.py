f=open(r'C:\Users\kanchana\Desktop\input.txt','r')
list1=[]
list2=[]
for line in iter(f):
	str1=line.split("=")
	list1=int(str1[1])
	list2.append(list1)
	
sum= list2[0]+list2[1]
#sum = str(sum) TypeError: 'str' object is not callable
sum=sum.__str__()
f1 =open(r'C:\Users\kanchana\Desktop\output.txt','w')	
f1.write(sum)
f1.close()
f.close()





