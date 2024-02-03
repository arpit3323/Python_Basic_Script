def exchange_list(number_list):
   
    num1=[]
    num2=[]
    
    num1=number_list[0:(len(number_list)//2)]
    num2=number_list[(len(number_list)//2):len(number_list)]
    num2.reverse()
    number_list=num2+num1
    
    
        
    
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
