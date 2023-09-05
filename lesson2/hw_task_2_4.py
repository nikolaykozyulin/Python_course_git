#Map method should be used

def compareList(list_1, list_2):
    res_list = list()
    for item_1 in list_1:
        for item_2 in list_2:
            if item_1 == item_2:
                res_list.append(item_1)
            else:
                print("I'm doing nothing")
    print(res_list)


def compareListFilter(list_1, list_2):
    res_list2 = list_2
    return print(list(filter(lambda x: x in list_1, res_list2)))


#print(list(filter(compareList(list_2), list_2)))


list_1 = ['one', 'two', '3', '4']
list_2 = ['3', 'two', '4']


compareList(list_1, list_2)
compareListFilter(list_1, list_2)

