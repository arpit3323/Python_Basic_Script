def bracket_pattern(input_str):

    count=0
    c=0

    if(input_str.startswith("(") and input_str.endswith(")")):
        for i in input_str:
            if(i=="("):
                count+=1
            else:
                c+=1

        if(c==count and c+count== len(input_str)):

            return True
    return False

input_str="(())"
print(bracket_pattern(input_str))
