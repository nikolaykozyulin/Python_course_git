#function for calculation factorials

#recursion factorial
def f(n):
    if n>=0:
        print("Factorial is defined")
        if n==0:
            result = 1
            print("Factorial = ", result)
        elif n>0:
            result=1
            for i in range(1,n+1):
                result *= i
            print("Factorial = ", result)
    else:
        print("Factorial is not defined")


print("Start")
print("Enter the number, n=")
n=int(input())
f(n)

