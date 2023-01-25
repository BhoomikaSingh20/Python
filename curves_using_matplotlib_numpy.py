def reverse_string(str1):    
    rev_str = ""
    for i in range(len(str1)-1,-1,-1):
        rev_str+=a[i]
    return rev_str

print("***** REVERSE A STRING *****")
ch = 'y'
while(ch=='y' or ch=='Y'):
    a = input("\nEnter a String: ")
    print("Reverse of ", a," is: ", reverse_string(a))

    ch = input("\nWant to continue?(y/n): ")
input()
