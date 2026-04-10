import re

def extract_date(text: str) -> list[str]:
    return [date for date in re.findall(r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})", text)]

if __name__ == "__main__":
    text = "Today is 10-04-2026, yesterday was 09-04-2026, invalid 2026-04-10"
    print(extract_date(text))
        