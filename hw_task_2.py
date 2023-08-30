#function compares lengths of two strings
def stringsComparison(s1,s2):
    if (len(s1) > len(s2)):
        print("STR with max lenght=")
        print(s1)
    elif (len(s1) < len(s2)):
        print("STR with max lenght=")
        print(s2)
    else:
        print("STRs have equal length=")
        print(s1)
        print(s2, '\n')
    print("End")


print("Please, Enter two strings", '\n')
print("s1= ")
s1 = input()
print("s2= ")
s2 = input()
stringsComparison(s1,s2)
