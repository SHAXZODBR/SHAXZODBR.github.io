def rightRotate(lists, num):
    output_list = []
 
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list

lst = [1, 2, 3, 5, 1, 2, 6, 7]
print(rightRotate(lst,5)) 