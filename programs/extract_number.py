import re

def extract_numbers(text: str) -> list[str]:
    result = re.findall(r"\d+", text)
    return result

if __name__ == "__main__":
    text = "Order 123, price 456, discount 20"
    print(extract_numbers(text))
    

    
    