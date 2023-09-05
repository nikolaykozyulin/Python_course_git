

def stopWordsControl(list_value):
    print(list(filter(lambda x: x in stop_list, list_value)))




stop_list = ['Python', 'php', 'go', 'C']
string_value = 'Python go to University'
list_value = string_value.split(" ")
print(list_value)

stopWordsControl(list_value)

