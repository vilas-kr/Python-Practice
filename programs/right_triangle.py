def right_triangle(n: int):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
        
if __name__ == "__main__":
    right_triangle(int(input("Enter a number : ")))