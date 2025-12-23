def is_disarium(number):
    """
    Check whether a number is a Disarium number.
    """
    digits = [int(d) for d in str(number)]
    total = sum(d ** (i + 1) for i, d in enumerate(digits))
    return total == number


def get_disarium_numbers(limit):
    """
    Generate all Disarium numbers up to a given limit.
    """
    return [n for n in range(1, limit + 1) if is_disarium(n)]



def main():
    print("=== Disarium Number Checker ===")
    print("1. Check a number")
    print("2. Generate Disarium numbers up to a limit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        num = int(input("Enter the number to check: "))
        if is_disarium(num):
            print(f"{num} is a Disarium number.")
        else:
            print(f"{num} is NOT a Disarium number.")
    elif choice == '2':
        limit = int(input("Find Disarium numbers up to: "))
        numbers = get_disarium_numbers(limit)
        print(f"Disarium numbers up to {limit}: {numbers}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()