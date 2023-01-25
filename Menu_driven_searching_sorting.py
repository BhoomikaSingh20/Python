#Program 11: Menu-driven program to accept a list of students names and perform:
# a. search element  using linear/binary search
# b. sort elements using bubble/insertion/selection sort

#linear search
def linear_search(lst, x):
    for i in range(len(lst)):
 
        if lst[i] == x:
            return i
 
    return -1

#Binary search
def binary_search(lst, low, high, x):
    if high >= low:
        mid = (high + low)//2
        if(lst[mid]==x):
                return mid
        elif(lst[mid]>x):
                return binary_search(lst, low, mid - 1, x)
        else:
                return binary_search(lst, mid + 1, high, x)
    else:
        return -1

#Selection sort
def selection_Sort(lst):
    for index in range(len(lst)):
        min_index = index
        for j in range(index + 1, len(lst)):
            # select the minimum element in every iteration
            if lst[j] < lst[min_index]:
                min_index = j
         # swapping the elements to sort the list
        lst[index], lst[min_index] = (lst[min_index], lst[index])

#Insertion sort
def insertion_Sort(lst):
    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key

#Bubble sort
def bubble_Sort(lst):
    n = len(lst)
    swap = False
    # Traverse through all array elements
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j + 1]:
                swap = True
                lst[j],lst[j + 1] = lst[j + 1], lst[j]
            if not swap:
                pass

ch="Y"
while (ch=="y" or ch=="Y"):
    size = int(input("\nEnter size of list: "))
    lst  = []
    for i in range(size):
        ele = eval(input("Enter name of student: "))
        lst.append(ele)
    print()
    print("*"*40)
    print("MENU")
    print("*"*40)
    print("1.Search element  using Linear/Binary search")
    print("2.Sort elements using Bubble/Insertion/Selection sort")

    choice=int(input("\nEnter your choice: "))

    if (choice==1):
        x = eval(input("Enter value to search in the given list: "))
        
        print("***** SEARCHING *****")
        print("1.Linear Search")
        print("2.Binary Search")

        option1=int(input("\nChoose an Option: "))
        print()
        if (option1==1):
            print(x, "is at", linear_search(lst,x)+1, "position.")
        elif(option1==2):
            result = binary_search(lst, 0, len(lst)-1, x)
            if (result!= -1):
                print("Element is present at position", str(result)+1)
            else:
                print("Element is not present in list")
        else:

            print("Invalid Option!")

    elif(choice==2):
        print("***** SORTING *****")
        print("1.Bubble Sort")
        print("2.Insertion Sort")
        print("3.Selection Sort")

        option2=int(input("\nChoose an Option: "))
        print()
        if (option2==1):
            bubble_Sort(lst)
            print(lst)
        elif(option2==2):
            insertion_Sort(lst)
            print(lst)
        elif(option2==3):
            selection_Sort(lst)
            print(lst)
        else:
            print("Invalid Option!")

    ch = input("\nWant to continue?(Y/N): ")

                            
    
