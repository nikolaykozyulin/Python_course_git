

def stopWordsControl(list_value):
    print(list(filter(lambda x: x in stop_list, list_value)))


stop_list = ['Python', 'php', 'go', 'C']
list_value = ['Python', 'go', 'to', 'University']
stopWordsControl(list_value)

