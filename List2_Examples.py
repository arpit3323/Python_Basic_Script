List=['G','E','E','K','S','F','O','R','G','E','E','K','S']
print("Initaial List:")
print(List)

Sliced_List=List[3:8]
print(Sliced_List)

Sliced_List=List[5:]
print(Sliced_List)


Sliced_List=List[:]
print(Sliced_List)


Sliced_List=List[:-2]
print(Sliced_List)

Sliced_List=List[-6:-1]
print(Sliced_List)


Sliced_List=List[::-1]

print(Sliced_List)


odd_square=[]

for x in range(1,11):
    if x % 2==1:
        odd_square.append(x**2)
print(odd_square)
