n=int(input("Enter a number="))

def fibonacci(a,b):
    global n
    if(n==0):
        return
    print(a)
    n-=1
    fibonacci(b,a+b)

fibonacci(0,1)

