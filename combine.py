import threading
import sys  # Import sys module

# Function to load English words from a dictionary file with a minimum word length
def load_dictionary(dictionary_file, min_word_length=1, num_words=50000):
    dictionary = []
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number > num_words:
                break
            word, _ = line.strip().split()  # Split the line into word and frequency
            word = word.lower()
            if len(word) >= min_word_length:
                dictionary.append(word)
    return dictionary

# Function to find individual dictionary words that can be made using a given string
def find_individual_words(input_string, dictionary):
    return [word for word in dictionary if all(input_string.count(c) >= word.count(c) for c in word)]

# Handler function to terminate the execution on timeout
def timeout_handler():
    print("Operation timed out. Try a shorter input or lower minimum word length.")
    sys.exit(0)  # Terminate the program inline

if __name__ == "__main__":
    dictionary_file = "en-2012/en.txt"  # Replace with the path to your dictionary file
    input_string = input("Enter the input string: ").lower()
    min_word_length = int(input("Enter the minimum word length: "))
    timeout_seconds = int(input("Enter the timeout in seconds: "))
    num_words = int(input("Enter dictionary size: "))  # Recommended 5000
    # block_word = input("Enter word to block from results: ").lower()

    # Load the first 50,000 words from the dictionary with the specified minimum word length
    dictionary = load_dictionary(dictionary_file, min_word_length, num_words)
    # dictionary.remove(block_word)

    # Set a timeout using a separate thread
    timeout_thread = threading.Timer(timeout_seconds, timeout_handler)
    timeout_thread.start()

    # Find individual dictionary words that can be made using the user's input
    words_found = find_individual_words(input_string, dictionary)
    print(words_found[:40])

    # Initialize a list to store combinations of words
    word_combinations = []

    # Helper function to find combinations of words that form the user's input
    def find_combinations(remaining_letters, current_combination, words_found_in):
        if not remaining_letters:
            word_combinations.append(current_combination)
            return

        # Create a copy of words_found to avoid modifying the original list
        local_words_found = list(words_found_in)
        for word in words_found_in:
            if all(remaining_letters.count(c) >= word.count(c) for c in word):
                new_remaining = remaining_letters
                for letter in word:
                    new_remaining = new_remaining.replace(letter, '', 1)
                find_combinations(new_remaining, current_combination + [word], local_words_found)
            # Remove the used word from local_words_found to avoid O(n!) algorithm.
            local_words_found.remove(word)

    find_combinations(input_string, [], words_found)

    if word_combinations:
        print("Combinations of words that form the user's input:")
        for combination in word_combinations:
            print(' '.join(combination))
    else:
        print("No valid combinations found.")

    # Cancel the timeout thread at the end of the program
    timeout_thread.cancel()
