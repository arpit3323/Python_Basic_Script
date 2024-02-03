def generate_dict(number):
	#start writing your code here
	new_dict={}
	for i in range(1,number+1):
	    new_dict[i]=i*i
	return new_dict

number=20
print(generate_dict(number))

