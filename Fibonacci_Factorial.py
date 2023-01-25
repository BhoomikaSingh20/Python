
#Program 3: Function to find nth term of fibonacci sequence and its factorial and return a list

def fib(n):
    #Fibonacci sequence
    n1, n2 = 0, 1
    count = 0
    fib_lst = [n1,n2]
    while(count<n-2):
        nth = n1+n2
        fib_lst.append(nth)
        n1 = n2
        n2 = nth
        count+=1
    return fib_lst

def factorial(n):
    #factorial of n
    prod = 1;
    for i in range(1,n+1):
        prod*=i
    return prod

def lst_fib_fact(num):
    fib_seq  = fib(num)
    fact_num = factorial(fib_seq[-1])
    #list of nth term of fibonacci sequence and its factorial 
    result   = []
    result.append(fib_seq[-1])
    result.append(fact_num)
    return result

print("----- FIBONACCI and FACTORIAL -----\n")
ch = 'y'
while (ch=='y' or ch=='Y'):
    x = int(input("Enter nth value: "))
    print("List of Fibonacci sequence and Factorial:")
    print(lst_fib_fact(x))

    ch = input("\nwant to continue?(y/n)")
