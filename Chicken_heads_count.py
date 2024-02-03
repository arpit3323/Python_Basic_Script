def solve(heads,legs):
    error_msg="No Solution"
    Chicken_count=0
    rabbit_count=0

    if heads==(legs/2):
        chicken_count=heads
    elif heads==(legs/4):
        rabbit_count=heads
    elif legs%2==0:
        rabbit_count=(legs//2)-heads
        chicken_count=heads-rabbit_count
    else:
        print(error_msg)

    if chicken_count>0 or rabbit_count>0:
        if chicken_count<=heads and rabbit_count<=heads:
            print(chicken_count,rabbit_count)
        else:
            print(error_msg)
solve(20,10)
