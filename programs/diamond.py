def diamond(n: int):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n-1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    diamond(10)