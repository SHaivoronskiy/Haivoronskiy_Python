def main():
    # Part 1: Check if the entered number is greater than 7
    try:
        number = float(input("Enter any number: "))
        if number > 7:
            print("Hello")
    except ValueError:
        print("Please enter a valid number.")

    # Part 2: Check if the entered name matches "John"
    name = input("Enter a name: ").strip()
    if name.lower() == "john":
        print("Hello, John")
    else:
        print("There is no such name")

    # Part 3: Print elements of the array that are multiples of 3
    try:
        array = list(map(int, input("Enter a numeric array (comma-separated values): ").split(',')))
        multiples_of_3 = [x for x in array if x % 3 == 0]
        if multiples_of_3:
            print("Elements that are multiples of 3:", multiples_of_3)
        else:
            print("No elements are multiples of 3.")
    except ValueError:
        print("Please enter a valid numeric array.")

if __name__ == "__main__":
    main()
