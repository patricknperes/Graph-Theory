import os


def clear_terminal():
    os.system("cls")


def pause_terminal():
    print("\n")
    os.system("pause")


def calculate_average(lst):
    if not lst:
        return None

    total_sum = 0

    for element in lst:
        total_sum += element

    average = total_sum / len(lst)
    return average


clear_terminal()
user_input = input("Enter a list of integers separated by space: ")
pause_terminal()

number_list = [int(item) for item in user_input.split()]

average_result = calculate_average(number_list)

clear_terminal()
if average_result is not None:
    print(f'The average of the numbers in the list is: {average_result}')
else:
    print('The list is empty. Cannot calculate the average.')

pause_terminal()
