def form_triangle(num1,num2,num3):
    success="Triangle can form"
    failure="Triangle can't form"

    a=num1+num2
    b=num1+num3
    c=num2+num3

    if a>num3 and b>num2 and c>num1:
        return success
    else:
        return failure

num1=8
num2=5
num3=15

print(form_triangle(num1,num2,num3))
