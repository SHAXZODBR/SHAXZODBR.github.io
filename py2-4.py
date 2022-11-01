def counter_dict(list):
    count={}
    for i in list:
        count.update({i:count.get(i,0)+1})
    return count

lst = [1, 2, 3, 5, 1, 2, 6, 7] 
print(counter_dict(lst))