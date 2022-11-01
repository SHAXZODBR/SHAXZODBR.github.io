lst = [1, 2, 3, 5, 1, 2, 6, 7] 
print("Input list : ",lst)
 
def distinct(li): 
    lst1 = [] 
    count = 0
    for i in lst: 
        if i not in lst1: 
            count = count + 1
            lst1.append(i) 
    print("Output list : ",lst1)
    print("No. of unique items are:", count)

distinct(lst) 