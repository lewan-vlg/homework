my_dict={'Nadia':1988,'Vasia': 1987,'Igor':1987}
print('Dict:',my_dict)
print('Existing value:', my_dict['Nadia'])
print('Not existing value:',my_dict.get('Oleg'))
del my_dict['Igor']
print(my_dict.get('Igor','Deleted value: 1987'))
my_dict.update({'Olga':1985, 'Misha': 1956})
print('Modified dictionary:',my_dict)

my_set={1,1,1,'пирог',1,2,6.6,1,2,1,1,2,1,1,1}
print('set:',my_set)
my_set.discard(1)
print('Modified set:',my_set)