from itertools import permutations

# Function to load the first 50,000 English words from a dictionary file
def load_dictionary(dictionary_file, num_words=50000):
    dictionary = []
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number > num_words:
                break
            word, _ = line.strip().split()  # Split the line into word and frequency
            dictionary.append(word.lower())
    return dictionary

# Function to find individual dictionary words that can be made using a given string
def find_individual_words(input_string, dictionary):
    return [word for word in dictionary if all(input_string.count(c) >= word.count(c) for c in word)]

if __name__ == "__main__":
    dictionary_file = "en-2012/en.txt"  # Replace with the path to your dictionary file
    input_string = input("Enter the input string: ").lower()

    # Load the first 50,000 words from the dictionary in order
    dictionary = load_dictionary(dictionary_file, num_words=50000)

    # Find individual dictionary words that can be made using the user's input
    words_found = find_individual_words(input_string, dictionary)

    # Initialize a list to store combinations of words
    word_combinations = []

    # Helper function to find combinations of words that form the user's input
    def find_combinations(remaining_letters, current_combination):
        if not remaining_letters:
            word_combinations.append(current_combination)
            return
        for word in words_found:
            if all(remaining_letters.count(c) >= word.count(c) for c in word):
                new_remaining = remaining_letters
                for letter in word:
                    new_remaining = new_remaining.replace(letter, '', 1)
                find_combinations(new_remaining, current_combination + [word])

    find_combinations(input_string, [])

    if word_combinations:
        print("Combinations of words that form the user's input:")
        for combination in word_combinations:
            print(' '.join(combination))
    else:
        print("No valid combinations found.")
