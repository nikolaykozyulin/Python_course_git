import time


def timer(f):
    def result(x):
        start_time = time.time()
        print(start_time)
        r = f(x)
        end_time = time.time()
        print(end_time)
        elapsed_time = end_time - start_time
        return print(f'Время выполнения функции = {elapsed_time}')
    return result


@timer
def square(number_values):
    return print(list(map(lambda x: x ** 2, number_values)))


number_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
square(number_values)
