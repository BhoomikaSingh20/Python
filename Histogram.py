def match_char(str1, str2):
    count = 0
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if(a[i]==b[j]):
                count+=1
    return count

print("***** NO. OF CHARACTERS MATCH IN TWO STRINGS *****")
ch = 'y'
while(ch=='y' or ch=='Y'):
    a = input("\nenter 1st string: ")
    b = input("enter 2nd string: ")

    print("\nNo. of characters match: ",match_char(a,b))

    ch = input("\nWant to continue?(y/n): ")

input()
