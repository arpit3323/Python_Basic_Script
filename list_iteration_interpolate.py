name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

z = zip(name, animal, age)

for name,animal,age in z:
    print("%s the %s is %s" % (name, animal, age))



ruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']

for idx,val in enumerate(ruit):
    print("%s: %s" % (idx, val))
