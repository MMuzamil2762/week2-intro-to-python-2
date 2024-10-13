def even_numbers(n):
    lst = []
    for element in n:
        if element % 2 == 0:
            lst.append(element)

    return lst
