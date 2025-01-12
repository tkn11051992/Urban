my_dict = {'Kirill': 1992, 'Maria': 1987}
print(my_dict.get('Kirill'))
print(my_dict.get('Ekaterina'))
my_dict.update({'Pavel': 1990, 'Marina': 1985})
a = my_dict.pop('Pavel')
print(a)
print(my_dict)
my_set = {1, 2, 1, 'Apple', 'Pear', 'Apple'}
print(my_set)
my_set.update([3, 4])
my_set.discard(1)
print(my_set)