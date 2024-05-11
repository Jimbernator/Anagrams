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




# Function to find combinations of words that form the user's input
def find_combinations(input_string, words_found):
    # Initialize an empty stack to keep track of word indices forming the combination
    stack = []
    # Initialize an empty list to store the word combinations
    word_combinations = []
    # Initialize a list to keep track of remaining letters after each word is used
    remaining_letters = [input_string]
    # Initialize the index to traverse the list of words
    index = 0

    # Continue looping until all combinations are explored
    while True:
        # Check if all words have been considered and the stack is empty
        if index == len(words_found) and not stack:
            break
        
        # If all words have been considered for the current combination,
        # pop the last index from the stack and restore the remaining_letters
        if index == len(words_found):
            index = stack.pop()
            remaining_letters.pop()
            index += 1
            # Run check agains
            continue

        # Retrieve the current word from the list of words
        word = words_found[index]
        # Check if the current word can be formed from the remaining letters
        if all(remaining_letters[-1].count(c) >= word.count(c) for c in word):
            # If so, add the index of the word to the stack
            stack.append(index)
            # Copy the remaining letters for the next word
            remaining_letters.append(remaining_letters[-1])
            # Remove the letters of the word from the remaining letters
            for letter in word:
                remaining_letters[-1] = remaining_letters[-1].replace(letter, '', 1)
            # If all letters are used, horay! we've found an anagram
            if not remaining_letters[-1]:
                # Construct the current combination and add it to word_combinations
                word_combinations.append([words_found[i] for i in stack])
        else:
            # Move to the next word only if the current word cannot be formed
            index += 1

    return word_combinations





if __name__ == "__main__":
    dictionary_file = "en-2012/en.txt"  # Replace with the path to your dictionary file
    if(1):
        input_string = input("Enter the input string: ").lower()
        min_word_length = int(input("Enter the minimum word length: "))
        timeout_seconds = int(input("Enter the timeout in seconds: "))
        num_words = int(input("Enter dictionary size: "))  # Recommended 5000
    else:
        input_string = "sirenbeans"
        min_word_length = 5
        timeout_seconds = 9
        num_words = 5000  # Recommended 5000
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

    # find_combinations(input_string, [], words_found)
    word_combinations = find_combinations(input_string, words_found)

    if word_combinations:
        print("Combinations of words that form the user's input:")
        for combination in word_combinations:
            print(' '.join(combination))
    else:
        print("No valid combinations found.")

    # Cancel the timeout thread at the end of the program
    timeout_thread.cancel()
