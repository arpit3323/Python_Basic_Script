my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])

print(my_list[3])

#Nested List
my_list1=["HAPPY",[2,3,15,5]]
print(my_list1[0][1])

print(my_list1[1][3])


#Negative Indexing
my_list2 = ['p','r','o','b','e']

print(my_list2[-1])
print(my_list2[-5])

# List slicing in Python

my_list3 = ['p','r','o','g','r','a','m','i','z']

print(my_list3[2:5])
print(my_list3[:-5])
print(my_list3[5:])
print(my_list3[:])


#add element

my_list3[0]=1
print(my_list3)


#append method

my_list3.append(2)
print(my_list3)

my_list3.extend([1,2,3])
print(my_list3)




# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd+[7,9,11])
print(["re"]*3)

print(len(odd))


# Deleting list items

my_list4 = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

del my_list4[2]
print(my_list4)

# List Reverse
systems = ['Windows', 'macOS', 'Linux']
print(systems)

systems.reverse()
print(systems.reverse())





# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list	
#Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list)
