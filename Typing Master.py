import time

def typing_master():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text as quickly and accurately as possible:")
    print(text)
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    correct_characters = sum(1 for a, b in zip(text, user_input) if a == b)
    accuracy = correct_characters / len(text)
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2%}")

typing_master()