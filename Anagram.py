import re
import itertools

# Function to load the English words and their frequencies from a dictionary file
def load_dictionary(dictionary_file):
    dictionary = set()
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line in file:
            word, _ = line.strip().split()
            dictionary.add(word.lower())
    return dictionary

# Function to generate anagrams
def generate_anagrams(input_string, dictionary):
    input_string = re.sub(r'[^a-zA-Z]', '', input_string).lower()
    results = []
    stack = [(('', input_string),)]

    while stack:
        try:
            (current_anagram, remaining_string), *rest = stack
        except ValueError:
            break  # Exit the loop if the stack is empty
        if not remaining_string:
            results.append(current_anagram)
        else:
            for word_length in range(1, len(remaining_string) + 1):
                for combination in itertools.permutations(remaining_string, word_length):
                    word = ''.join(combination)
                    if word in dictionary:
                        new_anagram = current_anagram + " " + word if current_anagram else word
                        new_remaining = remaining_string.replace(word, '', 1)
                        stack.append((new_anagram, new_remaining))

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
