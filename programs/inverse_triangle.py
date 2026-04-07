def inverse_triangel(n: int):
    for i in range(n,-1,-1):
        print(" " * (n - i) + "*" * (2 * i + 1))
        
if __name__ == "__main__":
    inverse_triangel(int(input("Enter a number : ")))
        