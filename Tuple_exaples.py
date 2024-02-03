lunch_menu=("Welcome Drink","Veg-starter","Non-veg starter","veg-main course","Non-veg Main Course","Dessert")

sample_tuple="A","B","C"
sample_tuple1=("D",)

print("Number of elements in the list, Lunch menu:",len(lunch_menu))

print("Element at 2nd position in lunch_menu:",lunch_menu[2])

print("Concatenating tuples:")

sample_tuple=sample_tuple+sample_tuple1
print(sample_tuple)


sample_tuple=sample_tuple1+("E",)
print(sample_tuple)


print("Iterating the tuple using keyword in")
for food_type in lunch_menu:
    print(food_type)

print("Searching for an element in tuple")
if "Dessert" in lunch_menu:
    print("Dessert is there")
else:
    print("Dessert is  not there")


print("tuple slice using positive indices:",lunch_menu[1:5])
print("tuple slice using negative indices:",lunch_menu[-5:-1])
