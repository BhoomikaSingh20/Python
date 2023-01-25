#Program 15: Define a class student to store name and marks in three subjects.
#use class variable to store maximum avergae marks of class.
#use constructor and destructor to initialize and destroy the objects.

class Student:
    #constructor to initialize values
    def __init__(self):
        self.lst_avg = []
        self.ch = 'y'
        while(self.ch=='y' or self.ch=='Y'):    
            self.name = input("\nEnter your name: ")
            self.sub1 = float(input("Enter marks in Python: "))
            self.sub2 = float(input("Enter marks in Data Structures : "))
            self.sub3 = float(input("Enter marks in Computer Network: "))
            self.avg  = (self.sub1+self.sub2+self.sub3)/3
            self.lst_avg.append(self.avg)

            self.ch = input("\nWant to continue?(Y/N): ")
    
    #method to store maximum average marks of class
    def max_avg_marks(self):
        max_avg = max(self.lst_avg)
        return max_avg

    #destructor to destroy variables
    def __del__(self):
        del self.name,self.sub1,self.sub2,self.sub3,self.avg,self.lst_avg,max_avg


s = Student()
print("\nMaximum Average Marks of Class is: ", s.max_avg_marks())

