#list can store homogeneous data
list_of_airlines=["AI","EM","BA"]
print("List of airlines:",list_of_airlines)

#list can  store heterogeneous data
sample_list=["Mark",5,"Jack",9, "Chan",5]
print("Sample List:",sample_list)

#Length of the list
print("Number of elements in the list:",len(sample_list))

#Random read
print("Element at 2nd index position:", sample_list[2])

#Random write
sample_list[2]="James"

#Random read
print("Element at 2nd index position after random write:",sample_list[2])


#Adding an element to list
sample_list.append("James")
print("After adding element to list:",sample_list)

#Combining two lists
new_list=["Henry","Tim"]
sample_list+=new_list

#Adds Henry and Tim to the existing sample_list
print("After combining two lists - 1st way:",sample_list)

#Another way to combine two lists
sample_list=sample_list+new_list

#Adds Henry and Tim to the new sample_list
print("After combining two lists - 2nd way:",sample_list)

#Accessing an element beyond the total number of elements in the list
print(sample_list[11])
#Will give you IndexError
