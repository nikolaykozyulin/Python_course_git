#function determites question or normal comments

def detQuestion(comment):
    last = comment[-1]
    if last == '?':
        print("It is question")
    else:
        print("Normal")
    print("End")


print("Please Enter Comment")
comment = input()
detQuestion(comment)
