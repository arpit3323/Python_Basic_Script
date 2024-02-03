import re
def find_upper_and_lower(sentence):

    count,c=0,0
    list=[]

    n=re.sub(r"\s![1-9]@","",sentence)

    print(n)
    for i in n:
        if(i.islower()):
            count+=1
        else:
            c+=1

    list.append(c)
    list.append(count)


    return list

sentence="Come Her2e"
print(find_upper_and_lower(sentence))
