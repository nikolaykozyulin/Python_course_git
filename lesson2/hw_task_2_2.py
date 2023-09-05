#function that returns list devides n


def num_list(n, list_values):
    print(list(filter(lambda x: x % n == 0, list_values)))


list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
num_list(n, list_values)
