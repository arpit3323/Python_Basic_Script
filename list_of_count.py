

def list_of_count(word_list):
   
    count_list=[]
    for i in range(len(word_list)):
        count_list.append(len(word_list[i]))
    
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))
