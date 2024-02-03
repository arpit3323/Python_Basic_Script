def create_largest_number(number_list):
    l=[]
    for i in range (0,len(number_list)):
        m=max(number_list)
        l.insert(i,str(m))
        number_list.remove(m)
    s=int("".join(l))
    return s
number_list=[23,94,55]
largest_number=create_largest_number(number_list)
print(largest_number)
