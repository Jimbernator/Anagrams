import re
from itertools import permutations

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

# Function to generate anagrams
def generate_anagrams(input_string, dictionary):
    input_string = re.sub(r'[^a-zA-Z]', '', input_string).lower()
    results = []

    # Generate all permutations of the input string
    permutations_list = [''.join(perm) for perm in permutations(input_string)]

    print("Permutations:", permutations_list[:5])

    # Filter valid anagrams
    for permuted_string in permutations_list:
        if permuted_string in dictionary:
            results.append(permuted_string)

    return results

if __name__ == "__main__":
    dictionary_file = "en-2012/en.txt"  # Replace with the path to your dictionary file
    input_string = input("Enter the input string: ")

    # Load the first 50,000 words from the dictionary
    dictionary = load_dictionary(dictionary_file, num_words=50000)

    print("Loaded Dictionary (First 5 entries):", list(dictionary)[:5])

    anagrams = generate_anagrams(input_string, dictionary)

    if anagrams:
        print("Anagrams found:")
        for anagram in anagrams:
            print(anagram)
    else:
        print("No valid anagrams found.")
