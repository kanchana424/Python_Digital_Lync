#List is denoted with [] and it can have any data type . Lists are mutable or changeable
#Definig a list
list1 =[1,2,"hi",4,5.12]

#Lists can have multiple lists inside, called nested lists
list2 =[1,2,3,["hi","hello"],[1.23,5.43]]

#Accesing each element in list  
# for i in list1:
#   print(i)
# for i in list2:
#     print(i)

# To check a particular value is available in list or not and print its index value
# if "hi" in list1:
#    print("Value exists")
#    print(list1.index("hi"))
# else:
#   print("Value doesn't exist")


#List comphrension, which prints the squares of a listed values

# list_sq =[1,2,3,4,5]

# sq = [i*i for i in list_sq]
# print(sq)

#Create a list with a range function

# list_range =[i for i in range(0,10)]
# print(list_range)

#Accessing every 3rd element in a list

# list_access =[1,2,3,4,5,6,7,8,9,10]
# i =0
# while i <len(list_access):
#     print(list_access[i])
#     i =i+3

#Assignig a list to another variable

# list3=list1
# print(list3)

#TO check the length of a list

# print(len(list1))

#Concatinate 2 lists

# list4 = list1 +list2
# print(list4)

#Converting list to string
# str_list=str(list1)
# print(str_list)
# print(type(str_list))

#As list is converted to string, concatinate works
# print(str_list +"34")

#Insert a value to a list by specifying a index
#list1.insert(0,22)
#print(list1)


#Append a value to the list, which appends at the end of the list
# list1.append("append")
# print(list1)
# list1.append(["new","value"])
# print(list1)


#Pop a value from list if index is specified, value at the index is removed, else last element is removed
# list1.pop(3)
# list1.pop()
# print(list1)


#How to remove a element-----Only the first instance of the value is removed
# list_rem =[1,2,3,4,"hi",5,1,2,"hi",3]
# list_rem.remove("hi")
# print(list_rem)

#How to remove repeated elements in list
# list_repeat =[1,2,3,4,5,1,2,5,6,7,7,8,3,1]
# list2_repeat=[]
# for i in list_repeat:
#     if i not in list2_repeat:
#         list2_repeat.append(i)
# print(list2_repeat)


#How to check how many times a element is repeated using count()
# list_repeat =[1,2,3,4,5,1,2,5,6,7,7,8,3,1]
# print(list_repeat.count(1))  #Count takes element value not index

#how to remove every 2nd element in the list *************************** when popped the index changes but i need to remove every 2nd element in main list
# list_remove =[1,2,3,4,5,1,2,5,6,7,7,8,3,1]
# i =0
# while i <len(list_remove):
#     list_remove.pop(i)
#     i =i +2
# print(list_remove)

#How to delete a index value*****************************************************we are not giving del.list() then how it works
# list1_del = ['hi','hello', "pen", "snake"];
# print(list1_del)
# del list1_del[2];
# print("After deleting value at index 2 : ")
# print(list1_del)


# How to add 2 lists without converting to strings and also using extend()
# list1_add =[1,2,3]
# list2_add =[4,5,6]
# print(list1_add+list2_add)
# list1_add.extend(list2_add)
# print(list1_add)
# list1_add.extend([7,8])
# print(list1_add)

#Compare elements in both lists***********************************************************************************************

# list1_cmp =[1,2,3,4,5]
# list2_cmp =[4,3,2,1]
# print(cmp(list1_cmp,list2_cmp))

#Print the max and minimum element of the list
# list1_max =[1,34,756,234,1111] #The list can contain only ints or strings but not both,"zi"]
# list2_max =["ji","lo","po","fo"]
# print(max(list1_max))
# print(max(list2_max))
# print(min(list1_max))
# print(min(list2_max))

#COnverting a tuple to list using seq()
# tuple_to_list =(1,2,3,4,"ji")
# print(type(tuple_to_list))
# tuple_list =list(tuple_to_list)
# print(tuple_list)
# print(type(tuple_list))

#Reversing a list using reverse()
# list1_rev =[1,2,3,4,5,6,7,8,9]
# list1_rev.reverse()
# print(list1_rev)

#Reversing a list using slice


#Sorting a list
# list_sort =[1,4,5,7,2,76,84,23,0,2]
# list_sort.sort()
# print(list_sort)


#How to print each character in a list element
# lists1=["hello","hi"]
# i =0
# j=0
# while j <len(list1):
#     print(lists1[i][j])
#     j=j+1

#How to print list of lists
# list1=["hi","hello",["ping","pong"]]
# print(list1[2][0]) #******************************************************************************************
# sub_list =list1[2][0]
# print(sub_list)

#slicing a list
# list_slice =[1,2,3,4,5,6,7,8]
# print(list_slice[:])
# print(list_slice[0:])
# print(list_slice[:-1])
# print(list_slice[0:4])
# print(list_slice[0:6:2])
# print(list_slice[-1::-1]) #Reversing list


# * operation on list
# list_op =[1,2,3]
# print(list_op*4)
# list2_op=[i*4 for i in list_op]
# print(list2_op)




