import json, random
from time import time

def main(): 
    with open('quotes.json', 'r') as file:
        data = json.load(file)
    quotes_no = len(data)
    again = 'y'

    while again == 'y': 
        random_no = random.randint(0, quotes_no - 1)
        q = data[random_no]
        sample_text = f'"{q["quote"]}" by {q["author"]}'

        text = []

        print('Press Enter to start typing and to break a new line')
        print('Press Enter twice to finish typing\n')
        print(sample_text)
        input('---------------------------------------------------')

        start = time()

        while True:
            line = input() 
            if not line:
                break
            text.append(line)

        end = time()

        print('---------------------------------------------------')

        elapsed_time = round((end - start), 2)

        # Join the lines of text into a single string
        user_input = '\n'.join(text)

        # Calculate character counts
        chars_count = sum(len(item) for item in text)
        word_count = chars_count / 5

        # Calculate accuracy
        correct_chars = sum(1 for i, char in enumerate(sample_text) if i < len(user_input) and char == user_input[i])
        accuracy = (correct_chars / len(sample_text)) * 100 if sample_text else 0
        WPM = round(word_count/ (elapsed_time/ 60), 2)

        # Print results
        print(f'Time taken: {elapsed_time} seconds')
        print(f'Characters typed: {chars_count}')
        print(f'Estimated words: {word_count:.2f}')
        print(f'Accuracy: {accuracy:.2f}%')
        print(f'Words per Minute: {WPM}')

        again = input("Would you like another quote? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for playing, and see you next time!")
            break 


if __name__ == '__main__':
    main()