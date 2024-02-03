def calculate_net_amount(trans_list):

    d,w=0,0
    for i in trans_list:
        n=i.split(":")
        if(n[0]=='D'):
            d=d+int(n[1])
        else:
            w=w+int(n[1])
    return d-w

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
