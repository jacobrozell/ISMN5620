
# Task 2


def get_numbers_less_than(k, list):
    newList = []
    for num in list:
        if num < k:
            newList.append(num)

    return newList


if __name__ == '__main__':
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    number = int(input("Enter a number that will be the ceiling number for the search: "))

    newList = get_numbers_less_than(number, list)

    print("-----Numbers Found With Input List " + str(list) + " and Ceiling Number " + str(number) + "-----")
    for num in newList:
        print(str(num))


