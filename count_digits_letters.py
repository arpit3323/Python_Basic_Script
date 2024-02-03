def count_digit_letters(sentence):

    co=0
    count=0
    result_list=[]

    sentence=sentence.replace(" ","")
    sentence=sentence.replace(";","")
    sentence=sentence.replace("-","")

    for i in sentence:
        if (i.isdigit()):
            co+=1
        else:
            count+=1
    result_list.append(count)
    result_list.append(co)
    return result_list

sentence="Infosys Mysore 570027"
print(count_digit_letters(sentence))
