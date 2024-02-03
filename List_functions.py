mark_list=[78,90,90,95,83,95]

mark_pos=mark_list.index(90)
print("Index position of mark 90:",mark_pos)

mark_list.append(54)
print("After adding new mark :", mark_list)

mark_list.insert(2,90)
print("After inserting 98 at the 2nd index position:",mark_list)

mark_list.pop(1)
print("After removing the mark at the 1st index position:",mark_list)

mark_list.sort()
print("After sorting the Marks in the given list:",mark_list)

mark_list.reverse()
print("After reversing marks in the given list:",mark_list)

list1 = ["e","d","u","c","a","t","i","o","n"]
print(list1[3:6])
