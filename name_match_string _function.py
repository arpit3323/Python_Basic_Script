def count_names(name_list):
    count1=0
    count2=0

    for i in name_list:
        if(i.endswith("at") and (i.startswith("at")!=i.endswith("at"))):
            count1+=1
        if(i.count("at")>0):
           count2+=1

    print("_at -> ",count1)
    print("%at% -> ",count2)

name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)
