import string
import re

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)

    clean_text = text.translate(translator)
    return clean_text


def clean_line(line):
    # Remove patterns like "Synonym 2:" or "2."
    line = re.sub(r'^(Synonym\s*\d+:\s*|\d+[\.:)\s]+)', '', line).strip()
    return line