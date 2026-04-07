def pyramid(n: int):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (i * 2 + 1))
        
if __name__ == "__main__":
    pyramid(int(input("Enter a number : ")))