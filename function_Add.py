Number = int(input("Enter how many numbers you want to add: "))

def calculate_sum(n):
    total = 0
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        total += num
    return print(f"The sum of the entered numbers is: {total}")


calculate_sum(Number)

