#Program 6: To perform various operations on Tuple, t1=(1,2,5,7,9,2,4,6,8,10)

def Tuple(t1,t2):
#(a)Tuple with even numbers
    lst=[]
    for i in range(len(t1)):
        if (t1[i]%2==0):
            lst.append(t1[i])
    print("Tuple with even numbers: ",tuple(lst))
    
#(b)Concatenate Tuple t2 with Tuple t1
    tup=t1+t2
    print("\nConcatenation of Tuple t1 and Tuple t2 : ",tup)
    
#(c)Maximum and Minimum from tuple tup
    print("\nMaximum of the Tuple t1: ",max(tup),"\nMinimum of the Tuple t2: ",min(tup))
    

t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
Tuple(t1,t2)
