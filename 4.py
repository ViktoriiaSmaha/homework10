def read_last(lines, file):
    with open(file) as file:
        line_list = file.readlines()
        length = len(line_list)
        first_element_index = length - lines
        for i in range(length):
            if i >= first_element_index:
                print(line_list[i])




read_last(4, "my_file.txt")