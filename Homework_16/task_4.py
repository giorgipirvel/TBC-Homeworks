def merge_list(list1,list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i = i + 1
        else:
            merged_list.append(list2[j])
            j = j + 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

list1 = [2,7,14,26]
list2 = [0,17,6,72]

merged_list = merge_list(list1,list2)
print(merged_list)
