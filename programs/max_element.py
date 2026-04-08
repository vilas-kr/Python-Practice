def find_max(arr: list[int]) -> int:
    max = arr[0]
    
    for i in arr[1:]:
        if max < i:
            max = i
    
    return max

if __name__ == "__main__":
    arr = [1, 2, 5, 3, 98, 29]
    print(find_max(arr))
    