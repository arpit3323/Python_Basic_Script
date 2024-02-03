phone=9876543234
a=str(phone)
print(a)
count=0

if(len(a))==10:
    print("valid")

if(a.startswith("9")):
    print("start with a ")

if(a[0]=="9"):
    print("start with 9")
    

for i in range(0,len(a)):
    if (a[i]=="6"):
      count=count+1
print(count)
