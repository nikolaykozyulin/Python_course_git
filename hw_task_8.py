#function that extract first litera

def extractLit(string):
    n = len(string)
    if n>0:
        print("String exists")
        print(string[0])
        for elem in range(n):
            if string[elem] == " ":
                print(string[elem+1])
    else:
        print("String is empty")




print("Please, Enter a few words")
string = input()
extractLit(string)
