def squares_of_evens(lst):
    sq_evens = []
    for element in lst:
        if element % 2 == 0:
            sq_evens.append(element ** 2)

    return sq_evens

