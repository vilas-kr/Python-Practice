import re 

def find_words_without_leading_digits(text: str) -> list[str]:
    return re.findall(r"\b[a-zA-Z]+\b", text)

if __name__ == "__main__":
    text = "abc1 test hello2 world python3 code"
    print(find_words_without_leading_digits(text))