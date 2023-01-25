#Program 7: To perform various operations on Strings

def func(str1):
    ch="Y"
    while (ch=="y" or ch=="Y"):
        print("*"*40)
        print("MENU")
        print("*"*40)
        print("1.Find the length of the string")
        print("2.Return maximum of three strings")
        print("3.Accept a string and replace all vowels with '#' ")
        print("4.Find the number of words in a given string")
        print("5.Check whether the string is a palindrome or not\n")

        choice=int(input("Enter your choice: "))

        if (choice==1):
            print("\nLength of ", str1, "is ",len(str1))

        elif (choice==2):
            str2=input("Enter string 2: ")
            str3=input("Enter string 3: ")
            str_lst = [str1,str2,str3]
            print("Maximum of three strings is: ", max(str_lst))

        elif (choice==3):
            string=input("\nEnter a string: ")
            vowels="aeiouAEIOU"
            for i in vowels:
                string=string.replace(i,"#")
            print(string)

        elif(choice==4):
            lst=str1.split()
            words = len(lst)
            print("\nNumber of words in given string is: ",words)
                
        elif(choice==5):
            revstr=str1[::-1]
            if str1==revstr:
                print("\n", str1, "is a Palindrome.")
            else:
                print("\n", str1, "is NOT a Palindrome.")
        else:
            print("\nError! Invalid choice!")
        
        ch = input("\nWant to continue?(Y/N): ")

str1=input("Enter string: ")
func(str1)
         

        
    
