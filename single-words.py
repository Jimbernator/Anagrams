# Function to load the first 50,000 English words from a dictionary file
def load_dictionary(dictionary_file, num_words=50000):
    dictionary = set()
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number > num_words:
                break
            word, _ = line.strip().split()  # Split the line into word and frequency
            dictionary.add(word.lower())
    return dictionary

if __name__ == "__main__":
    dictionary_file = "en-2012/en.txt"  # Replace with the path to your dictionary file
    input_string = input("Enter the input string: ").lower()

    # Load the first 50,000 words from the dictionary
    dictionary = load_dictionary(dictionary_file, num_words=50000)

    # Find individual dictionary words that can be made using the user's input
    words_found = [word for word in dictionary if all(input_string.count(c) >= word.count(c) for c in word)]

    if words_found:
        print("Individual dictionary words found:")
        for word in words_found:
            print(word)
    else:
        print("No valid dictionary words found.")
