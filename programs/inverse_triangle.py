def inverse_triangle(n: int):
    for i in range(n, 0, -1):
        print("*" * (2 * i - 1))

if __name__ == "__main__":
    inverse_triangle(int(input("Enter a number : ")))