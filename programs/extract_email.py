import re

def extract_emails(text: str) -> list[str]:
    return [x for x in re.findall(r"\w+@\w+\.\w{2,}", text)]

if __name__ == "__main__":
    text = "Contact: test@gmail.com, admin@yahoo.in, invalid@com, user@domain.co"
    print(extract_emails(text))