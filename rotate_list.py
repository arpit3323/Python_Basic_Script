
def rotate_list(input_list,n):
   
    l=len(input_list)
    m=l-n
    
    return input_list[m:]+input_list[0:m]
    
    
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
