def palindrome_dict(string):
    dict_str = {x: x[::-1] for x in string.split(" ")}
    return dict_str
if __name__ == "__main__":
    sentence = "Hello, how are you?"
    dict_sentence = palindrome_dict(sentence)
    print(dict_sentence)
