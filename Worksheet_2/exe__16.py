def anagram_check(word1,word2):
    if len(word1)!=len(word2):
        return False
    else:
        if sorted(word1)==sorted(word2):
            return True

def main():
    string_1=input("Enter the first string: ")
    string_2=input("Enter the second string: ")
    if not string_1 or not string_2:
        print("Please enter both strings")
    elif string_1.strip()=="" or string_2.strip()=="" :
        print("Please enter both strings")
    elif string_1==string_2:
        print("The strings are equal, they are not anagrams")
    else:
        if anagram_check(string_1,string_2):
            print("The strings are anagrams")
        else:
            print("The strings are not anagrams, they should be of equal length")

if __name__ == '__main__':
    main()
