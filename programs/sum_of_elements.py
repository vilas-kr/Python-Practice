def sum_of_elements(arr: list[int]) -> int:
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(sum_of_elements(arr))