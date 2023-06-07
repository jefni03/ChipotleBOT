import re
import time

def find_word_between_text_to(line):
    match = re.search(r'Text\s+(\w+)\s+to', line, re.IGNORECASE)  # Adding re.IGNORECASE flag for case insensitivity
    if match:
        return match.group(1)
    else:
        return None

def read_log_file(file_path, encodings=('utf-8', 'latin-1')):
    found_words = set()
    while True:
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    for line in file:
                        word = find_word_between_text_to(line)
                        if word and word not in found_words:
                            found_words.add(word)
                            print(word)
                break  # Exit the encoding loop after processing the file once
            except UnicodeDecodeError:
                continue
        time.sleep(1)  # Wait for 1 second before checking the file again

# Example usage
log_file_path = r'C:\Users\Jeffrey\AppData\Local\Google\Chrome\User Data\Default\Platform Notifications\000006.log'
read_log_file(log_file_path)
