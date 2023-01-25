#prorgam 22: Implementation of Selection sort, Insertion sort and Bubbel sort

#Selection sort
def selection_Sort(lst, size):
    for index in range(size):
        min_index = index
        for j in range(index + 1, size):
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

ch = 'y'
while(ch=='y' or ch=='Y'):
    n = int(input("Enter the number of elements: "))
    lst = []
    for i in range(n):
        ele = int(input("Element: "))
        lst.append(ele)
    print("1. Selection sort\n 2. Insertion sort\n 3. Bubble sort\n")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        selection_Sort(lst, n)
        print('The list after sorting in Ascending Order by selection sort is:')
        print(lst)
    elif(choice==2):
        insertion_Sort(lst)
        print('The list after sorting in Ascending Order by selection sort is:')
        print(lst)
    elif(choice==3):
        bubble_Sort(lst)
        print('The list after sorting in Ascending Order by selection sort is:')
        print(lst)
    else:
        print("Invalid choice!")

    ch = input("Want to continue?(y/n): ")
