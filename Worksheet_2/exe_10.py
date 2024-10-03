def string_concatenate(s1,s2):
    if s1.strip() == "" and s2.strip() == "":
        return 'Both strings are empty'
    else:
        return s1+s2
def main():
    string_1=input("Enter the first string: ")
    string_2=input("Enter the second string: ")
    print(string_concatenate(string_1,string_2))

if __name__ == '__main__':
    main()
