import time
import random

def typing_tester():
    sample_texts = [
        "def add(a, b): return a + b",
        "for i in range(10): print(i)",
        "if x > 0: print('Positive') else: print('Negative')",
        "class Dog: def __init__(self, name): self.name = name",
        "try: x = int(input()) except ValueError: print('Invalid input')"
    ]

    sample_text = random.choice(sample_texts)
    
    print("\nWelcome to the Python Syntax Typing Speed Test!")
    print("You will be given a Python code snippet to type. Let's see how fast and accurate you are!")
    print("\nType the following code:\n")
    print(sample_text + "\n")

    input("Press Enter to start typing...")

    start_time = time.time()

    user_input = input("\nYour input: ")

    end_time = time.time()

    time_taken = end_time - start_time

    words_typed = len(user_input) / 5  
    typing_speed_wpm = words_typed / (time_taken / 60)

    correct_chars = sum(1 for i in range(min(len(sample_text), len(user_input))) if sample_text[i] == user_input[i])
    accuracy = (correct_chars / len(sample_text)) * 100

    if len(user_input) > len(sample_text):
        accuracy -= (len(user_input) - len(sample_text)) / len(sample_text) * 100
    print("\nResults:")
    print("Typing speed: {:.2f} words per minute".format(typing_speed_wpm))
    print("Accuracy: {:.2f}%".format(accuracy))

typing_tester()
