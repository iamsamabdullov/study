def list_pull(L):
    lst = []
    for element in L:
        if type(element) is list:
            lst.extend(list_pull(element))
        else:
            lst.append(element)
    return lst
print(list_pull([['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]))


