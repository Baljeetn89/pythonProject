def remove_odd_numbers(numbers):
    """Returns a list with all odd numbers removed."""
    return [num for num in numbers if num % 2 == 0]


def main():
    """Tests the remove_odd_numbers function."""
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
    filtered_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("List after removing odd numbers:", filtered_list)


if __name__ == "__main__":
    main()