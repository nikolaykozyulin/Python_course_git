def int_decorator(f):
    def result(x):
        try:
            r = f(x)
        except Exception as ex:
            print("Exception call")
            print(ex)
        finally:
            r = f(x)
    return result


@int_decorator
def square_list(list_values):
    #list_values ** 2
    return print(list(map(lambda x: x ** 2, list_values)))


@int_decorator
def print_list(word_list):
    print(word_list)


@int_decorator
def square_number(number):
    return print(number ** 2)



#def no_space(word_list):
#    return print(word_list)


list_values = [1, 2, 3, 4]
word_list = "Monday Evening"
square_list(list_values)
square_number(10)
print_list(word_list)