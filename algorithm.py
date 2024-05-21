def main():
    # If the entered number is greater than 7, then print “Hello”
    number = float(input("Enter any number: "))
    if number > 7:
        print("Hello")

    # If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

    # There is a numeric array at the input, it is necessary to output array elements that are multiples of 3
    array_input = input("Enter a numeric array (use comma between values): ")
    array_comma = array_input.split(',')
    array = []

    for element in array_comma:
        array.append(int(element))

    mult3 = []

    for number in array:
        if number % 3 == 0:
            mult3.append(number)

    if mult3:
        print("Numbers that are multiples of 3:", mult3)
    else:
        print("No number are multiples of 3.")

if __name__ == "__main__":
    main()