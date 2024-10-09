def search(input_str,word_search):
    repeats=input_str.count(word_search)
    return repeats

def main():
    str_input = input("Enter a sentence: ")
    word=input("Enter a word to search for: ")
    if not str_input or not word:
        print("Check whether you gave both inputs required to search")
    else:
        print(search(str_input,word),"Time's,", word, " word occurred in a given sentence: " , str_input)

if __name__ == "__main__":
    main()
