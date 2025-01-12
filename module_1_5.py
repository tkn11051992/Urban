immutable_var = 1, "арбуз"
print(immutable_var)
#immutable_var[0] = 2 (нельзя изменить значения элементов кортежа, так как кортеж не поддерживает обращение по элементам)
mutable_list = ([2, "дыня"])
mutable_list[1] = "банан"
print(mutable_list)