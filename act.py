v={"a1":"apple", "b2":"ball", "c3":"cat", "d4":"dog"}

print(v)

#Updating Dictionary
v["e5"]="elephant"
print(v)

var_to_extract=['b2','c3','d4', 'e5']

#Slicing
sliced_dict = {var: v[var] for var in var_to_extract}

print(sliced_dict)