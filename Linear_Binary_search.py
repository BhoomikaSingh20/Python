#prorgam 21: Implementation of Linear and Binary Search Techniques

#Linear Search
def linear_Search(lst1, size_of_lst, key):  
    for i in range(0, size_of_lst):  
        if (lst1[i] == key):  
            return i  
    return -1  

#Binary Search
def binary_Search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # to get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
        elif list1[mid] > n:  
            high = mid - 1   
        else:  
            return mid
    return -1  

ch = 'y'
while(ch=='y' or ch=='Y'):  
    n = int(input("Enter the number of elements: "))
    lst = []
    for i in range(n):
        ele = int(input("Element: "))
        lst.append(ele)
    key = int(input("Value to search: "))

    print("1. Linear Search \n 2. Binary Search\n")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        result = linear_Search(lst, n, key)
        if(result == -1):  
            print("Element not found")  
        else:  
            print("Element found at index: ", result)
    elif(choice==2):
        result = binary_Search(lst, n)
        if(result == -1):  
            print("Element not found")  
        else:  
            print("Element found at index: ", result)
    else:
        print("Invalid choice!")
 
    
    ch = input("Want to continue?(y/n): ")
