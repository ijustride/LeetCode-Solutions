def digit_root(n):
    # Congruence formula for getting a digital root of given integer 'n'
    return (n - 1) % 9 + 1 if n else 0


def main():
    # 38 -> 3 + 8 = 11 -> 1 + 1 = 2
    # no loop/recursion and time complexity O(1)
    n = 38
    print(digit_root(n))


if __name__ == "__main__":
    main()
