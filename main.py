def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split()
        length = len(words)
        print(length)
        
        def char_count(str):
            hash = {}
            str = str.lower()
            for i in range(len(str)):
                 if str[i] in hash:
                     hash[str[i]] += 1
                 else:
                     hash[str[i]] = 1
            print(hash)
        char_count(file_contents)
main()

