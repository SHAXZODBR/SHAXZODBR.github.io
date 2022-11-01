def rev_manual_index_loop(mylist):
    a = []
    reverse_index = len(mylist) - 1
    for index in range(len(mylist)):
        a.append(mylist[reverse_index - index])
    return a

lst = [1, 2, 3, 5, 1, 2, 6, 7]     
print(rev_manual_index_loop(lst))