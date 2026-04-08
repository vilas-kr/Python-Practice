def even_odd_count(arr: list[int]):
    even = odd = 0
    for num in arr:
        if num%2 == 0:
            even += 1
        else:
            odd += 1
            
    return even, odd

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    even, odd = even_odd_count(arr)
    print(f"Even Count : {even} \nOdd count : {odd}")