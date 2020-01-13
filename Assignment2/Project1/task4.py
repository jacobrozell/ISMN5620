
# HW Hints

# Task 4


def get_overlapping_numbers(list1, list2):
    return [x for x in list1 if x in list2]


def save_data_to_list(file_path):
    array = []
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            array.append(int(line.replace("\n", "")))
            line = fp.readline()

    return array


if __name__ == '__main__':
    path1 = input("Enter path to first file: ")
    array1 = save_data_to_list(path1)
    path2 = input("Enter path to second file: ")
    array2 = save_data_to_list(path2)

    print(get_overlapping_numbers(array1, array2))


