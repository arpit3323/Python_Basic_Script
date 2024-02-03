list=[12,34,45,54]
def check_digit(list):
    count=0

    for i in list:
        if i%10==(i+1)%10:
            return "Yes"
        else:
            return "NO"


print(check_digit(list))
