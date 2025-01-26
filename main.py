
def sort_on(char_dict):
    return char_dict["num"]
def char_count(input_str):
    # First create the dictionary of counts
    char_dict = {}
    input_str = input_str.lower()
    

    for char in input_str:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    # Sorting logic here
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
        char_list.sort(reverse=True, key=sort_on)
    print(char_list)
    return char_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split()
        length = len(words)
        chars = char_count(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{length} words found in the document")
        print()  # Add a blank line for formatting
        
        for char_dict in chars:

            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
            
        print("--- End report ---")

main()

