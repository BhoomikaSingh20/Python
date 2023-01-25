# program 8: function to take a number with two or more digits and reverse it, then compute sum of the digits

def reverse_and_sum(num):
    rev = ""
    sum = 0
    for i in range(len(str(num))-1,-1, -1):
        rev+=str(num)[i]
    print("Reverse of ", num, " is: ", int(rev))
    for i in range(len(str(num))):
        sum+=int(str(num)[i])
    print("Sum of ", num, " is: ", sum)
    return


print("----- REVERSE A NUMBER AND SUM OF ITS DIGITS -----")
ch = 'y'
while(ch=='y' or ch=='Y'):
    num = int(input("\nEnter a two or more digit number: "))
    reverse_and_sum(num)

    ch = input("\nwant to continue?(y/n): ")
    
input()
