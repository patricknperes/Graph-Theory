import os


def clear_terminal():
    os.system("cls")


def pause_terminal():
    print("\n")
    os.system("pause")


clear_terminal()
salary = float(input("Enter your current salary R$ "))
while salary < 0:
    print("Invalid salary. Please try again.\n")
    salary = float(input("Enter your current salary R$ "))

print("Your current salary is R$ {:.2f} per month.".format(salary))
pause_terminal()

clear_terminal()
print("Printing the income tax according to the provided salary.\n")

if salary <= 1903.98:
    print("Exempt from income tax")
elif salary <= 2826.65:
    print("Your income tax will be R$ {:.2f}.".format(salary * 0.075))
elif salary <= 3751.05:
    print("Your income tax will be R$ {:.2f}.".format(salary * 0.15))
elif salary <= 4664.69:
    print("Your income tax will be R$ {:.2f}.".format(salary * 0.225))
else:
    print("Your income tax will be R$ {:.2f}.".format(salary * 0.275))

pause_terminal()
