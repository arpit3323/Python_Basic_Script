def list123(nums):

    j=1
    c=0

    for i in nums:
        if i is j:
            j+=1
            c+=1
            if c==3:
                return True
    return False

nums=[1,2,3,4,5]
print(list123(nums))
