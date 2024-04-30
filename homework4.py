immutable_var = (12, "String", True, [1,2])
print("immutable_var ",immutable_var)
mutable_list= [12, "String", True]
print("mutable_list ",mutable_list)
mutable_list[0] = 'Mihail'
mutable_list.extend([1,2])
print("mutable_list ",mutable_list)