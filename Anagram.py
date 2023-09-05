import re

# Function to load the English words and their frequencies from a dictionary file
def load_dictionary(dictionary_file):
    dictionary = {}
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line in file:
            word, frequency = line.strip().split()
            dictionary[word.lower()] = int(frequency)
    return dictionary

# Function to generate anagrams
def generate_anagrams(input_string, dictionary):
    input_string = re.sub(r'[^a-zA-Z]', '', input_string).lower()
    results = []

    # Recursive function to find anagrams
    def find_anagrams(current_anagram, remaining_string, current_frequency):
        if not remaining_string:
            results.append(current_anagram)
            return

        for word in dictionary:
            if remaining_string.startswith(word):
                new_anagram = current_anagram + " " + word if current_anagram else word
                new_remaining = remaining_string[len(word):]
                new_frequency = current_frequency + dictionary[word]
                find_anagrams(new_anagram, new_remaining, new_frequency)

    find_anagrams('', input_string, 0)
    return results

if __name__ == "__main__":
    dictionary_file = "en-2012/en.txt"  # Replace with the path to your dictionary file
    input_string = input("Enter the input string: ")

    dictionary = load_dictionary(dictionary_file)
    anagrams = generate_anagrams(input_string, dictionary)

    if anagrams:
        print("Anagrams found:")
        for anagram in anagrams:
            print(anagram)
    else:
        print("No valid anagrams found.")
