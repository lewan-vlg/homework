my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
pozit = []
dex = 0
while dex<len(my_list):
    if (my_list[dex]<0): break
    elif my_list[dex] >0:
        pozit.append(my_list[dex])
        dex += 1
    elif my_list[dex] == 0:
        dex += 1
print(pozit)
