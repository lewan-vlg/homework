def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5, 'другая строка', False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list=[1, False, "труд"]
values_dict = {'a': "vine", 'b': {1, 2, 3, 4, 5, 9}, 'c': 34}
print_params(*values_list),
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)