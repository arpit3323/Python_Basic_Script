def encode(message):
    st=message+"0"
    l=[]
    count=1

    for i in range(0,len(st)-1):
        if st[i]==st[i+1]:
            count=count+1
        else:
            l.append(str(count))
            l.append(st[i])
            count=1
    s="".join(l)
    return s

encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
