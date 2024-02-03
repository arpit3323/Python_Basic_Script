def generate_sentences(subjcts,verbs,objects):
    list=[]
    for i in subjects:
        for j in verbs:
            for k in objects:
                list.append(i+" "+j+" "+k)
    return list

subjects=["I","You"]
verbs=["love","play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
