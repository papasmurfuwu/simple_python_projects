from time import time

# Sample text for the typing test
sample_text = "In the heart of the bustling city, where the streets were alive with the hum of activity, there stood an old bookstore."
text = []

print('Press Enter to start typing and to break a new line')
print('Press Enter twice to finish typing')
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