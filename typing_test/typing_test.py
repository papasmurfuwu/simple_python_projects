import json
import random
import os 
from time import time


def load_quotes(filename):
    """Load quotes from a JSON file."""
    base_dir = os.path.dirname(__file__) # special built-in variable in Python that contains the path of the script being executed
    abs_file = os.path.join(base_dir, 'quotes.json')

    try:
        with open(abs_file, encoding="utf-8") as file:
            return json.load(file)
        
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        return []


def calculate_results(sample_text, user_input, elapsed_time):
    """Calculate typing results."""
    chars_count = sum(len(item) for item in user_input)
    word_count = chars_count / 5
    correct_chars = sum(1 for i, char in enumerate(sample_text) if i < len(user_input) and char == user_input[i])
    accuracy = (correct_chars / len(sample_text)) * 100 if sample_text else 0
    WPM = round(word_count / (elapsed_time / 60), 2)

    return elapsed_time, chars_count, word_count, accuracy, WPM


def main():
    quotes = load_quotes('quotes.json')
    if not quotes:
        return  # Exit if no quotes are loaded

    again = 'y'
    while again == 'y':
        random_quote = random.choice(quotes)
        sample_text = f'"{random_quote["quote"]}" by {random_quote["author"]}'

        print('Press Enter to start typing and to break a new line')
        print('Press Enter twice to finish typing\n')
        print(sample_text)
        input('---------------------------------------------------')

        start = time()
        text = []

        while True:
            line = input()
            if not line:
                break
            text.append(line)

        end = time()
        elapsed_time = round((end - start), 2)

        print('---------------------------------------------------')

        user_input = '\n'.join(text)
        results = calculate_results(sample_text, user_input, elapsed_time)

        print(f'Time taken: {results[0]} seconds')
        print(f'Characters typed: {results[1]}')
        print(f'Estimated words: {results[2]:.2f}')
        print(f'Accuracy: {results[3]:.2f}%')
        print(f'Words per Minute: {results[4]}')

        again = input("Would you like another quote? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for playing, and see you next time!")


if __name__ == '__main__':
    main()
