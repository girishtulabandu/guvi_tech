import sys
from math import ceil, sqrt


def is_prime(n: int) -> bool:
    """Returns True iff n is prime."""
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False

    limit = ceil(sqrt(n))

    for factor in range(3, limit + 1, 2):
        if n % factor == 0:
            return False

    return True


if __name__ == '__main__':
    try:
        num = int(input("Check prime: "))
    except ValueError:
        print(f"Invalid")
        sys.exit(1)

    print('Yes' if is_prime(num) else 'No')
