def find_max(num1,num2):
    max_num=-1

    l=[max_num]

    if num1<num2:
        for i in range(num1,num2+1):
            if len(str(i))==2:
                sum=0
                for num in str(i):
                    sum=sum+int(num)

                if sum%3==0:
                    if i%5==0:
                        l.append(i)
    return max(l)

max_num=find_max(3,30)
print(max_num)
