# Program: prog Assing_8 - Lists
# Date: Oct. 31, 2026
# Git hub link https://github.com/lewisjohnson229/Prog-Assign_8---Lists/blob/main/main.py

# Defines the main function that holds the program
def main():

    # Create an empty list to store the numbers
    numbers = []

    # Ask the user to enter 20 numbers
    for count in range(20):
        number = float(input(f"Enter number {count + 1}: "))
        numbers.append(number)

    # Find the lowest and highest numbers
    lowest = min(numbers)
    highest = max(numbers)

    # Find the total and average
    total = sum(numbers)
    average = total / len(numbers)

    # Display the results to the user
    print("\n--- Number Analysis ---")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average:.2f}")

# Calls the main function to start the program
main()
