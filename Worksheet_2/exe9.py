def alternate_string(s):
    if s.strip()=="":
        return 'String is empty'
    else:
        return s[0::2]

def main():
    string_input=input("Enter a string: ")
    alternate=alternate_string(string_input)
    print(alternate)

if __name__ == '__main__':
    main()
