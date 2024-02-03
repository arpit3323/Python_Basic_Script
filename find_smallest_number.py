

def find_smallest_number(num):
    
    for i in  range(1,num*10):

        l=[]
        for j in range(1,i+1):
            if i%j==0:
                l.append(j)
                #count+=1
        if len(l)==num:
            return i

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
