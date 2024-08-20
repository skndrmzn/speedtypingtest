import time
import random

def typing_tester():
    # List of Python syntax sample texts to choose from
    sample_texts = [
        "def add(a, b): return a + b",
        "for i in range(10): print(i)",
        "if x > 0: print('Positive') else: print('Negative')",
        "class Dog: def __init__(self, name): self.name = name",
        "try: x = int(input()) except ValueError: print('Invalid input')"
    ]

    # Select a random sample text
    sample_text = random.choice(sample_texts)
    
    print("\nWelcome to the Python Syntax Typing Speed Test!")
    print("You will be given a Python code snippet to type. Let's see how fast and accurate you are!")
    print("\nType the following code:\n")
    print(sample_text + "\n")

    # Wait for the user to start
    input("Press Enter to start typing...")

    # Start timer
    start_time = time.time()

    # Get user input
    user_input = input("\nYour input: ")

    # End timer
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time

    # Calculate typing speed in WPM (words per minute)
    words_typed = len(user_input) / 5  # Average word length is 5 characters
    typing_speed_wpm = words_typed / (time_taken / 60)

    # Calculate accuracy
    correct_chars = sum(1 for i in range(min(len(sample_text), len(user_input))) if sample_text[i] == user_input[i])
    accuracy = (correct_chars / len(sample_text)) * 100

    # Handle case where user input is longer or shorter than the sample text
    if len(user_input) > len(sample_text):
        accuracy -= (len(user_input) - len(sample_text)) / len(sample_text) * 100

    # Print results
    print("\nResults:")
    print("Typing speed: {:.2f} words per minute".format(typing_speed_wpm))
    print("Accuracy: {:.2f}%".format(accuracy))

# Run the typing tester
typing_tester()
