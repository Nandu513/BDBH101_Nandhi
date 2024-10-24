def string_occurrence(s,c):
    if c.strip() == "" :
        return 'No letter is given to search'
    elif s.count(c)==0 :
        return 'letter is not found'
    else:
        occur = s.index(c)
        print(f"The first occurrence of {c} letter is in the position/element:")
        return occur+1

def main():
    string_input=input("Enter a string: ")
    search=input("Enter a letter to search for : ")
    if string_input.strip() == "" :
        return 'String is empty'
    else:
        print(string_occurrence(string_input,search))

if __name__ == '__main__':
    main()
