import time

def test_typing_speed():
    print("Type the following sentence:")
    sentence = "The quick brown fox jumps over the lazy dog"
    print(sentence)
    input("Press enter to start typing...")

    start_time = time.time()

    user_input = input()

    end_time = time.time()

    elapsed_time = end_time - start_time
    words = user_input.split()
    words_per_minute = len(words) / elapsed_time * 60

    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f}")

if __name__ == '__main__':
    test_typing_speed()
