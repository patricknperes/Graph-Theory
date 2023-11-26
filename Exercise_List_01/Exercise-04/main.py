import os


def find_element_position(lst, num):
    if not lst:
        return None

    for index, element in enumerate(lst):
        if element == num:
            return index
    return -1


os.system("cls")

user_input_list = input(
    "Enter a list of integers separated by space: ")
number_list = [int(item) for item in user_input_list.split()]

number_to_find = int(input("Enter the number you want to find in the list: "))

result = find_element_position(number_list, number_to_find)

if result is not None:
    if result != -1:
        print(f'The entered number is at position {result}')
    else:
        print("The number was not found in the list. Unable to return the position.")
else:
    print("The list is empty. Unable to return the position.")
