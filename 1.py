
def change(lst):
    first = lst[0]
    length = len(lst)
    last = lst[length - 1]
    lst[0] = last
    lst[length - 1] = first


print(change(["1", "2","3","4","7"]))