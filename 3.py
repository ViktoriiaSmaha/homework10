def sum_range(start, end):
    if start > end:
        start, end = end, start
    lst = []
    summ = 0
    current = start
    while current <= end:
        lst.append(current)
        current = current + 1
        summ = current + summ

    return summ


print(sum_range(4, 3))

