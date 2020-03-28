def load_data(data):
    results = []
    try:
        with open(data) as my_file:
            while True:
                line = my_file.readline()
                if line:
                    my_list = []
                    for elem in line:
                        if elem != ' ' and elem != '\n':
                            my_list.append(elem)
                    results.append(my_list)
                else:
                    break
    except FileNotFoundError as error:
        print("File not found")
        raise error
    return results


def load_info(some_list):
    some_dict = {}
    line_counter = 0
    for line in some_list:
        elem_counter = 0
        if type(line) == list:
            for elem in line:
                my_key = str(line_counter) + str(elem_counter)
                some_dict[my_key] = {"elem_path": '', "elem_sum": 0}
                elem_counter += 1
        line_counter += 1
    return some_dict


def get_size(data):
    size = len(data)
    return size


def fill_self(data_in, data_out):
    total_rows = get_size(data_in)
    current_row = total_rows - 1
    while current_row >= 0:
        max_index = current_row
        current_index = 0
        while current_index <= max_index:
            self_key = str(current_row) + str(current_index)

            my_path = str(data_in[current_row][current_index])
            my_sum = data_in[current_row][current_index]

            data_out[self_key]['elem_path'] = my_path
            data_out[self_key]['elem_sum'] = int(my_sum)

            current_index += 1
        current_row -= 1


def find_min(data_in, data_out):
    total_rows = get_size(data_in)
    current_row = total_rows - 2

    while current_row >= 0:
        max_index = current_row
        current_index = 0
        while current_index <= max_index:

            self_val = int(data_in[current_row][current_index])
            self_key = str(current_row) + str(current_index)

            left_val = int(data_in[current_row + 1][current_index])
            left_key = str(current_row + 1) + str(current_index)
            left_out = data_out[left_key]

            right_val = int(data_in[current_row + 1][current_index + 1])
            right_key = str(current_row + 1) + str(current_index + 1)
            right_out = data_out[right_key]

            if left_val < right_val:
                data_out[self_key]['elem_path'] = str(self_val) + left_out['elem_path']
                data_out[self_key]['elem_sum'] = self_val + left_out['elem_sum']
            else:
                data_out[self_key]['elem_path'] = str(self_val) + right_out['elem_path']
                data_out[self_key]['elem_sum'] = self_val + right_out['elem_sum']

            # there may be also 3rd case when 2 paths have the same sum
            # but I decided to return only one of them

            current_index += 1
        current_row -= 1


def print_credits(sign='*'):
    my_date = "Code written: 22.03.20"
    author = "Author: Jakub Jonczyk"
    if len(my_date) > len(author):
        size = len(my_date)
    else:
        size = len(author)
    line = size*sign
    print("\n{}\n{}\n{}\n{}\n".format(line, my_date, author, line))



files = ['tiny.txt', 'small.txt']

for file in files:
    pyramid = load_data(file)
    pyramid_data = load_info(pyramid)
    fill_self(pyramid, pyramid_data)
    find_min(pyramid, pyramid_data)

    print(file)
    print(f"Min sum is {pyramid_data['00']['elem_sum']}")
    print(f"Min path is {pyramid_data['00']['elem_path']}")
    print('\n')

print_credits()
