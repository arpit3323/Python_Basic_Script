#lex_auth_012693749623193600122

def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    while(number>0):
        rem=number%10
        sum_of_digits+=rem
        number=number//10
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
