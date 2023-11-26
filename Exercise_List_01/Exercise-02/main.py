import os


def clear_terminal():
    os.system("cls")


def pause_terminal():
    print("\n")
    os.system("pause")


clear_terminal()
square_side = int(
    input("Enter an integer to generate a square of *: "))
pause_terminal()

clear_terminal()
print("Printing the square.\n")

for i in range(1, square_side + 1):
    if i == 1 or i == square_side:
        print(f"{i} {'* ' * (square_side - 1)}*")
    else:
        print(f"{i} *{' ' * (2 * (square_side - 2) + 1)}*")

print()

for i in range(square_side):
    for j in range(square_side):
        if i == 0 or i == square_side - 1:
            print("* ", end='')
        elif j == 0 or j == square_side - 1:
            print("* ", end='')
        else:
            print("  ", end='')
    print("")
pause_terminal()
