def add_string(str1):

    length=len(str1)

    if length > 2:
        if str1[-3:]== 'ing':
            str1+='ly'
        else:
            str1+='ing'
    return str1

str1="sleep"
print(add_string(str1))

str1="amazing"
print(add_string(str1))

str1="is"
print(add_string(str1))
