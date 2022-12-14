def to_dict(lst):
    dict = {}
    for i in lst:
        dict.update({i: i})
    print(dict)


to_dict(["Lana","Jane"])
