#function that selects str type

def str_filter(str_list):
    print(list(filter(lambda x: isinstance(x, str), str_list)))


str_list = ['one', 'two', 3, 4, 'five', 6]
str_filter(str_list)

