import re

def count_words(title:str) -> int:
    words = re.findall(r'\b\w+\b', title)
    return len(words)