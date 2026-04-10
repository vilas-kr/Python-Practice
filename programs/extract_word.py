import re

def extract_word_starts_with_capital(text):
    return [w for w in re.findall(r"[A-Z]\w*", text)]

if __name__ == "__main__":
    text = "My name is Vilas and I live in Bangalore"
    print(extract_word_starts_with_capital(text))